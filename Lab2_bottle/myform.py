import re
from bottle import post, request, template
from datetime import datetime
import pdb
import json

questions = {}  # создаем словарь

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
        error_msg = "Invalid email address"
        return template("index.tpl", msg=error_msg, year=datetime.now().year)

    if len(question) <= 3 or question.isdigit():
        error_msg = "Question should have more than 3 characters and should not consist of only digits"
        return template("index.tpl", msg=error_msg, year=datetime.now().year)

    access_date = datetime.now().strftime("%Y-%m-%d")
    if mail in questions:
        questions[mail][0] = username
        if question not in questions[mail][1:]:
            questions[mail].append(question)
        else:
            error_msg = "This question has already benn asked by this user"
            return template("index.tpl", msg=error_msg, year=datetime.now().year)
    else:
        questions[mail] = [username, question]

    with open('questions.json', 'w') as json_file:
        json.dump(questions, json_file, indent=4)

    success_msg = f"Thanks, {username}! The answer will be sent to the mail {mail}. Access Date: {access_date}"
    return template("index.tpl", msg=success_msg, year=datetime.now().year)
