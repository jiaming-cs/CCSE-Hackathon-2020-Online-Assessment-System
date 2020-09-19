#!venv/bin/python
import os
from flask import Flask, url_for, redirect, render_template, request, abort, flash, session
from flask_sqlalchemy import SQLAlchemy
from flask_security import Security, SQLAlchemyUserDatastore, UserMixin, RoleMixin, login_required, current_user, RegisterForm
from flask_security.utils import encrypt_password
import flask_admin
from flask_admin.contrib import sqla
from flask_admin import helpers as admin_helpers
from flask_admin import BaseView, expose
from flask_admin.actions import action
from utility.email_sender import EmailSender
from utility.assessment_form import AssessmentForm
from const import SCORE_MAP, SCORE_CATEGORY_DICT, TOTAL_SCORE
from wtforms import StringField
from wtforms.validators import DataRequired
from datetime import datetime
from utility.generate_random_password import gen_password


# Create Flask application
app = Flask(__name__)
app.config.from_pyfile('config.py')
db = SQLAlchemy(app)


# Define models
roles_users = db.Table(
    'roles_users',
    db.Column('user_id', db.Integer(), db.ForeignKey('user.id')),
    db.Column('role_id', db.Integer(), db.ForeignKey('role.id'))
)


class Survey(db.Model):
    id = db.Column(db.Integer(), primary_key=True)
    first_name = db.Column(db.String(255))
    last_name = db.Column(db.String(255))
    email = db.Column(db.String(255), unique=True)
    suggestion = db.Column(db.String(1024))
    history_scores = db.Column(db.String(512))
    current_score = db.Column(db.Integer())
    rank = db.Column(db.Integer())
    active = db.Column(db.Boolean())
    def __str__(self):
        return self.email
    
    def __getitem__(self, field):
        return self.__dict__[field]



class Role(db.Model, RoleMixin):
    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String(80), unique=True)
    description = db.Column(db.String(255))

    def __str__(self):
        return self.name


class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(255))
    last_name = db.Column(db.String(255))
    email = db.Column(db.String(255), unique=True)
    password = db.Column(db.String(255))

    active = db.Column(db.Boolean())
    confirmed_at = db.Column(db.DateTime(), default=datetime.utcnow)
    roles = db.relationship('Role', secondary=roles_users,
                            backref=db.backref('users', lazy='dynamic'))

    def __str__(self):
        return self.email
    
    def __getitem__(self, field):
        return self.__dict__[field]


class ExtendedRegisterForm(RegisterForm):
    first_name = StringField('First Name', [DataRequired()])
    last_name = StringField('Last Name', [DataRequired()])

# Setup Flask-Security
user_datastore = SQLAlchemyUserDatastore(db, User, Role)
security = Security(app, user_datastore, register_form=ExtendedRegisterForm)


# Create customized model view class
class MyModelView(sqla.ModelView):

    def is_accessible(self):
        if not current_user.is_active or not current_user.is_authenticated:
            return False

        if current_user.has_role('superuser'):
            return True

        return False

    def _handle_view(self, name, **kwargs):
        """
        Override builtin _handle_view in order to redirect users when a view is not accessible.
        """
        if not self.is_accessible():
            if current_user.is_authenticated:
                # permission denied
                abort(403)
            else:
                # login
                return redirect(url_for('security.login', next=request.url))


    # can_edit = True
    edit_modal = True
    create_modal = True    
    can_delete = False
    can_edit = False
    can_create = False



class SurveyView(MyModelView):
    def is_accessible(self):
        if not current_user.is_authenticated:
            return False

        else:

            return True
    column_editable_list = []
    column_searchable_list = column_editable_list
    column_exclude_list = ['history_scores']
    # form_excluded_columns = column_exclude_list
    column_details_exclude_list = column_exclude_list
    column_filters = column_editable_list
    
    edit_modal = False
    edit_modal = False
    create_modal = False    
    can_export = False
    can_view_details = True
    details_modal = True
    
class UserView(MyModelView):
    column_editable_list = ['email', 'first_name', 'last_name']
    column_searchable_list = column_editable_list
    column_exclude_list = ['password']
    # form_excluded_columns = column_exclude_list
    column_details_exclude_list = column_exclude_list
    column_filters = column_editable_list
    

    
    @action('email', 'Email', 'Are you sure you want to email selected users?')
    def action_email(self, ids):
        es = EmailSender()
        try:
            to_list = []
            query = User.query.filter(User.id.in_(ids))
            for user in query.all():
                
                renewed_password = gen_password()
                user.password = encrypt_password(renewed_password)
                to_list.append((user.first_name, user.email, renewed_password))
                db.session.add(user)
                db.session.commit()
            es.send_invitation(to_list, "http://34.71.141.43/")
            flash("success")

        except Exception as ex:
            if not self.handle_view_exception(ex):
                raise

            flash("Failed")

from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField
from wtforms.validators import DataRequired, Length, Email, Required


class AssessmentView(BaseView):
    @expose('/', methods=['GET', 'POST'])
    def index(self):
        
        form = AssessmentForm(request.form)
        if request.method == 'POST' and form.validate():
            
            user_id = session['_user_id']
            user = db.session.query(User).filter(User.id == user_id).first()
            user_first_name = user['first_name']
            user_last_name = user['last_name']
            user_email = user['email']
            
            survey_user = db.session.query(Survey).filter(Survey.email == user_email)
            score = 0

            suggestions_dict = {}
            for i, filed in enumerate(form):
                if i < 5:
                    score += SCORE_MAP[filed.data]
                else:
                    max_score, category = SCORE_CATEGORY_DICT[i+60]
                    if SCORE_MAP[filed.data] < max_score:
                        suggestions_dict[category] = suggestions_dict.get(category, 0) + max_score - SCORE_MAP[filed.data]
                    else:
                        score += SCORE_MAP[filed.data]

            # score = int((score / TOTAL_SCORE) * 100)

            rank = db.session.query(Survey).filter((Survey.current_score > score) & (Survey.email != user_email)).count()+1

            suggestion = "\n".join(list(suggestions_dict.keys()))
            if survey_user.count() == 0:
                survey_user = Survey(first_name = user_first_name, last_name = user_last_name, email = user_email, current_score = score, history_scores = str(score), rank = rank, active = False, suggestion = suggestion)  
            else:
                survey_user = survey_user.first()
                survey_user.current_score = score
                survey_user.history_scores += ", "+str(score)
                survey_user.rank = rank
                survey_user.suggestion = suggestion
            db.session.add(survey_user)
            db.session.commit()
            
            # renew rank for every one:
            for user in db.session.query(Survey).all():
                rank = db.session.query(Survey).filter((Survey.current_score > user.current_score) & (Survey.email != user.email)).count()+1
                user.rank = rank
                db.session.add(user)
                db.session.commit()

            es = EmailSender()
            es.send_score(user_first_name, user_email, score, suggestions_dict)
            flash("You have successfully submitted your assessment!", "success")

            return self.render('admin/assessment_done_index.html')

        return self.render('admin/assessment_index.html', form=AssessmentForm())


# Flask views
@app.route('/')
def index():
    return render_template('index.html')

def get_admin_display_info(db):
    
    if current_user.is_authenticated:
        total_user = db.session.query(User).count()
        user_finished_survey = db.session.query(Survey).count()
        higest_score = db.session.query(db.func.max(Survey.current_score)).scalar()
        lowest_score = db.session.query(db.func.min(Survey.current_score)).scalar()


        return dict(total_user = total_user, user_finished_survey = user_finished_survey, highest_score = higest_score, lowest_score = lowest_score)


def get_user_display_info(db):
    if current_user.is_authenticated:
        user_id = session['_user_id']
        user = db.session.query(User).filter(User.id == user_id).first()
        user_email = user['email']
        survey_user = db.session.query(Survey).filter(Survey.email == user_email)
        if survey_user.count() == 0:
            return dict(score = "N/A", rank = "N/A", above = "N/A", attempts = 0)
        else:
            survey_user = survey_user.first()
            score = survey_user.current_score
            rank = survey_user.rank
            above = int(survey_user.rank / db.session.query(Survey).count() * 100)
            attempts = len(survey_user.history_scores.split(", "))
            return dict(score = score, rank = rank, above = above, attempts = attempts)

"""
Add anything you wanna to pass to the jinja template here!
"""
@app.context_processor
def inject_paths():
    
    return dict(user_display_info = get_user_display_info(db), admin_display_info = get_admin_display_info(db))

# Create admin
admin = flask_admin.Admin(
    app,
    'Online Assessment',
    base_template='my_master.html',
    template_mode='bootstrap3',
)

# Add model views
admin.add_view(MyModelView(Role, db.session, menu_icon_type='fa', menu_icon_value='fa-server', name="Roles"))
admin.add_view(UserView(User, db.session, menu_icon_type='fa', menu_icon_value='fa-users', name="Users"))
admin.add_view(SurveyView(Survey, db.session, menu_icon_type='fa', menu_icon_value='fa-pencil-square-o', name="Survey"))
admin.add_view(AssessmentView(name="Assessment", endpoint='assessment', menu_icon_type='fa', menu_icon_value='fa-file-text',))

# define a context processor for merging flask-admin's template context into the
# flask-security views.

@security.context_processor
def security_context_processor():
    return dict(
        admin_base_template=admin.base_template,
        admin_view=admin.index_view,
        h=admin_helpers,
        get_url=url_for
    )

def build_sample_db():
    """
    Populate a small db with some example entries.
    """

    import string
    import random

    db.drop_all()
    db.create_all()

    with app.app_context():
        user_role = Role(name='user')
        super_user_role = Role(name='superuser')
        db.session.add(user_role)
        db.session.add(super_user_role)
        db.session.commit()

        test_user = user_datastore.create_user(
            first_name='Admin',
            email='admin',
            password=encrypt_password('admin'),
            roles=[user_role, super_user_role]
        )

        first_names = [
            'Harry', 'Amelia', 'Oliver', 'Jack', 'Isabella', 'Charlie', 'Sophie', 'Mia',
            'Jacob', 'Thomas', 'Emily', 'Lily', 'Ava', 'Isla', 'Alfie', 'Olivia', 'Jessica',
            'Riley', 'William', 'James', 'Geoffrey', 'Lisa', 'Benjamin', 'Stacey', 'Lucy'
        ]
        last_names = [
            'Brown', 'Smith', 'Patel', 'Jones', 'Williams', 'Johnson', 'Taylor', 'Thomas',
            'Roberts', 'Khan', 'Lewis', 'Jackson', 'Clarke', 'James', 'Phillips', 'Wilson',
            'Ali', 'Mason', 'Mitchell', 'Rose', 'Davis', 'Davies', 'Rodriguez', 'Cox', 'Alexander'
        ]

        for i in range(len(first_names)):
            tmp_email = first_names[i].lower() + "." + last_names[i].lower() + "@example.com"
            tmp_pass = ''.join(random.choice(string.ascii_lowercase + string.digits) for i in range(10))
            user_datastore.create_user(
                first_name=first_names[i],
                last_name=last_names[i],
                email=tmp_email,
                password=encrypt_password(tmp_pass),
                roles=[user_role, ]
            )
        db.session.commit()
    return

if __name__ == '__main__':

    # Build a sample db on the fly, if one does not exist yet.
    app_dir = os.path.realpath(os.path.dirname(__file__))
    database_path = os.path.join(app_dir, app.config['DATABASE_FILE'])
    if not os.path.exists(database_path):
        build_sample_db()

    # Start app
    app.run(debug=True)