import re
from bottle import post, request, template
from datetime import datetime
import pdb

questions ={} #создаем словарь

@post('/home', method='post')
def my_form():
    mail = request.forms.get('ADRESS')
    username = request.forms.get('USERNAME')
    question = request.forms.get('QUEST') 

    if not mail or not username:
        error_msg = "Please fill in all fields"
        return template("index.tpl", msg=error_msg, year=datetime.now().year)

    email_pattern = r'^[a-zA-Z0-9._]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    if not re.match(email_pattern, mail):
        error_msg =  "Invalid email address"
        return template("index.tpl", msg=error_msg, year=datetime.now().year)

    access_date = datetime.now().strftime("%Y-%m-%d")
    success_msg =  f"Thanks, {username}! The answer will be sent to the mail {mail}. Access Date: {access_date}"
    questions[mail] = [username, question]
    pdb.set_trace()
    return template("index.tpl", msg=success_msg, year=datetime.now().year)