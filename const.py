EMAIL_USER_NAME = "magmutualassessment@gmail.com"
EMAIL_PASS_WORD = "test123456!"

INVITATION_EMAIL_TEMPLATE = '''
Dear {name}, 
<br>
<br> 
<p>You are invited to take Magmutual online assessment.</p>
<br>
<p>Please login using your email: <b>{email}</b>
<br>
password: <b>{password}</b>
<br>
on <a href = {link}>this link</a></p>
<br>
<p>Contact us if you have any other concerns!</p>
<br>
<p>Best Regards,</p>
<br>
<p>Magmutual Online Assessment Team</p>
'''

SCORE_NOTIFICATION_EMAIL_TEMPLATE = '''
Dear {name}, 
<br>
<br> 
<p>Thank you for taking the survey.</p>
<br>
<p>Your automatically evaluated score is <b>{score}</b>.</p>
<br>
<p>To improve your score, you need to concern more about fllowing issues:<br><br>{suggestions}<br><br></p>
<br>
<img src="cid:chart">
<br>
<p>Best Regards,</p>
<br>
<p>Magmutual Online Assessment Team</p>
'''

SCORE_MAP = {'Criteria Met':3,
'Partial Compliance':2,
'Criteria Not Met':1,
'Always':4,
'Almost Never':1,
'Never':0,
'Almost Always':3,
'Sometimes':2,
'NA':0,
True:0
}

TOTAL_SCORE = 646

SCORE_CATEGORY_DICT = {65: (3, 'HIPAA Privacy and Security'), 66: (3, 'HIPAA Privacy and Security'), 67: (3, 'HIPAA Privacy and Security'), 68: (3, 'HIPAA Privacy and Security'), 69: (3, 'HIPAA Privacy and Security'), 70: (3, 'HIPAA Privacy and Security'), 71: (3, 'HIPAA Privacy and Security'), 72: (3, 'HIPAA Privacy and Security'), 73: (3, 'HIPAA Privacy and Security'), 74: (3, 'HIPAA Privacy and Security'), 75: (3, 'HIPAA Privacy and Security'), 76: (3, 'HIPAA Privacy and Security'), 77: (3, 'ACA and Non-Discrimination'), 78: (3, 'ACA and Non-Discrimination'), 79: (3, 'ACA and Non-Discrimination'), 80: (3, 'ACA and Non-Discrimination'), 81: (3, 'ACA and Non-Discrimination'), 82: (3, 'ACA and Non-Discrimination'), 83: (3, 'ACA and Non-Discrimination'), 84: (3, 'OSHA'), 85: (3, 'OSHA'), 86: (3, 'OSHA'), 87: (3, 'OSHA'), 88: (3, 'OSHA'), 89: (3, 'OSHA'), 90: \
(3, 'OSHA'), 91: (3, 'OSHA'), 92: (3, 'OSHA'), 93: (3, 'OSHA'), 94: (3, 'Employment Practices'), 95: (3, 'Employment Practices'), 96: (3, 'Employment Practices'), 97: (3, 'Employment Practices'), 98: (3, 'Employment Practices'), 99: (3, 'Employment Practices'), 100: (3, 'Employment Practices'), 101: (3, 'Treatment of Minors'), 102: (3, 'Treatment of Minors'), 103: (3, 'Medications Use and Safety'), 104: (3, 'Medications \
Use and Safety'), 105: (3, 'Medications Use and Safety'), 106: (3, 'Medications Use and Safety'), 107: (3, 'Medications Use and Safety'), 108: (3, 'Medications Use and Safety'), 109: (3, 'Medications Use and Safety'), 110: (3, 'Medications Use and Safety'), 111: (3, 'Medications Use and Safety'), 112: (3, 'Medications Use and Safety'), 113: (3, 'Medications Use and Safety'), 114: (3, 'Medications Use and Safety'), 115: (3, 'Medications Use and Safety'), 116: (3, 'Medications Use and Safety'), 117: (3, 'Medications Use and Safety'), 118: (3, 'Medications Use and Safety'), 119: (3, 'Medications Use and Safety'), 120: (3, 'Medications Use and Safety'), 121: (3, 'Medications Use and Safety'), 122: (3, 'Medications Use and Safety'), 123: (3, 'Medications Use and Safety'), 124: (3, 'Medications Use and Safety'), 125: (3, 'Medications Use and \
Safety'), 126: (4, 'Medications Use and Safety'), 127: (3, 'Medications Use and Safety'), 128: (3, 'Medications Use and Safety'), 129: (3, 'Medications Use and Safety'), 130: (3, 'Medications Use and Safety'), 131: (3, 'Medications Use and Safety'), 132: (3, 'Medications Use and Safety'), 133: (3, 'Medications Use and Safety'), 134: (3, 'Medications Use and Safety'), 135: (3, 'Medications Use and Safety'), 136: (4, 'Medications Use and Safety'), 137: (3, 'Use of Chaperones'), 138: (3, 'Use of Chaperones'), 139: (3, 'Use of Chaperones'), 140: (3, 'Use of Chaperones'), 141: (3, 'Use of Chaperones'), 142: (3, 'Office Emergencies'), 143: (3, 'Office Emergencies'), 144: (3, 'Office Emergencies'), 145: (3, 'Office Emergencies'), 146: (3, 'Informed Consent'), 147: (3, 'Informed Consent'), 148: (4, 'Informed Consent'), 149: (3, 'Informed Consent'), 150: (3, 'Termination of the Provider-Patient Relationship'), 151: (3, 'Termination of the Provider-Patient Relationship'), 152: (3, 'Termination of the Provider-Patient Relationship'), 153: (3, 'Termination of the Provider-Patient Relationship'), 154: (3, 'Procedures Performed in the Medical Office'), 155: (3, 'Procedures Performed in the Medical Office'), 156: (3, 'Procedures Performed in the Medical Office'), 157: (3, 'Procedures Performed in the Medical Office'), 158: (3, 'Infection Control and Prevention'), 159: (3, 'Infection Control and Prevention'), 160: (3, 'Infection Control and Prevention'), 161: (3, 'Infection Control and Prevention'), 162: (3, 'Infection Control and Prevention'), 163: (3, 'Infection Control and Prevention'), 164: (3, 'Infection Control and Prevention'), 165: (3, 'Infection Control and Prevention'), 166: (3, 'Infection Control and Prevention'), 167: (3, 'Referral Management and Test Tracking'), 168: (3, 'Referral Management and Test Tracking'), 169: (3, 'Referral Management and Test Tracking'), 170: (3, 'Referral Management and Test Tracking'), 171: (3, 'Referral Management and Test Tracking'), 172: (3, 'Referral Management and Test Tracking'), 173: (3, 'Referral Management and Test Tracking'), 174: (3, 'Referral Management and Test Tracking'), 175: (3, 'Referral Management and Test Tracking'), 176: (3, 'Referral Management and Test Tracking'), 177: (3, 'Equipment Safety'), 178: (3, 'Equipment Safety'), 179: (3, 'Equipment Safety'), 180: (3, 'Health Information Management'), 181: (3, 'Health Information Management'), 182: (3, 'Health Information Management'), 183: (3, 'Health Information Management'), 184: (3, 'Health Information Management'), 185: (3, 'Health Information Management'), 186: (3, 'Health Information Management'), 187: (3, 'Health Information Management'), 188: (3, 'Health Information Management'), 189: (3, 'Health Information Management'), 190: (3, 'Health Information Management'), 191: (4, 'Health Information Management'), 192: (3, 'Risk Management'), 193: (3, 'Risk Management'), 194: (3, 'Risk Management'), 195: (3, 'Risk Management'), 196: (3, 'Risk Management'), 197: (3, 'Risk Management'), 198: (3, 'Record Audit'), 199: (3, 'Record Audit'), 200: (3, 'Record Audit'), 201: (3, 'Record Audit'), 202: (3, 'Record Audit'), 203: (3, 'Record Audit'), 204: (3, 'Record Audit'), 205: (3, 'Record Audit'), 206: (3, 'Record Audit'), 207: (3, 'Record Audit'), 208: (3, 'Record Audit'), 209: (3, 'Record Audit'), 210: (3, 'Record Audit'), 211: (3, 'Record Audit'), 212: (3, 'Record Audit'), 213: (3, 'Record Audit')}