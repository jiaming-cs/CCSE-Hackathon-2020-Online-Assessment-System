# Hackathon-2020

This repository is built for [KSU CCSE 2020 Hackathon](https://ccse.kennesaw.edu/events/hackathon.php) Magmutual Challenge of team 2Young2Simple.


## Functionalities
* Risk Consultant can send the assessment requests out via email to policy holders. Then medical doctor (policy holder) can log into the system, take the assessment and submit.  
![Email Sending](Graphs/email_sending.gif)

* System can capture the answers from a Likert scale and assign a score, then store it into the database.  
![Do the Survey](Graphs/survey.gif)

* System is also able to automatically generate the report after taking the assessment and send recommendation back to the selected policy holder.   
![Auto Grade & Result Visualization](Graphs/feed_back.gif)

* Medical doctor can compare his scores with his peers who have also taken the assessment and see his risk score ranking.  
![Login & Dashboard & Back Stage Management](Graphs/longin_dashboard.gif)


## Usage

### Setup Virtual Evironment
Conda:
```
conda create -n venv python=3.7
conda activate venv
pip install -r requirements.txt
```
OR

Virtualenv:

On Windows:

```
virtualenv venv --python=3.7
cd venv/Scripts 
activate
cd ../..
pip install -r requirements.txt
```

On Linux:

```
virtualenv venv --python=3.7
source venv/bin/activate
pip install -r requirements.txt
```

Run the server:
```
python app.py
```

## Citation

Web base frame work is adopted from [@jonalxh](https://github.com/jonalxh/Flask-Admin-Dashboard)
