import re
from bottle import post, request
from datetime import datetime

@post('/home', method='post')
def my_form():
    mail = request.forms.get('ADRESS')
    username = request.forms.get('USERNAME')

    if not mail or not username:
        return "Please fill in all fields"

    email_pattern = r'^[a-zA-Z0-9._]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'

    if not re.match(email_pattern, mail):
        return "Invalid email address"

    access_date = datetime.now().strftime("%Y-%m-%d")
    return "Thanks, {}! The answer will be sent to the mail {}. Access Date: {}".format(username, mail, access_date)