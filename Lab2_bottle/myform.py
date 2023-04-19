import re
from bottle import post, request, template
from datetime import datetime
import pdb
import json

questions ={} #создаем словарь

@post('/home', method='post')
def my_form():
    mail = request.forms.get('ADRESS')
    username = request.forms.get('USERNAME')
    question = request.forms.get('QUEST') 
    access_date = datetime.now().strftime("%Y-%m-%d")

    if not mail or not username:
        error_msg = "Please fill in all fields"
        return template("index.tpl", msg=error_msg, year=datetime.now().year)

    email_pattern = r'^[a-zA-Z0-9._]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    if not re.match(email_pattern, mail):
        error_msg =  "Invalid email address"
        return template("index.tpl", msg=error_msg, year=datetime.now().year)
    else:
        if len(question) < 4 or question.isdigit():
            message = "Invalid question text or text is too short"
        else:
            if mail in questions:
                if question in questions[mail]:
                    message = "This question has already been asked"
                else:
                    questions[mail].append(question) 
                    with open("questions.json", "a") as quest_file:
                        json.dump(questions, quest_file, indent = 4)
                    message =  f"Thanks, {username}! The answer will be sent to the mail {mail}. Access Date: {access_date}"
            else:
                questions[mail] = [question]
                with open("questions.json", "a") as quest_file:
                    json.dump(questions, quest_file, indent = 4)
                message = f"Thanks, {username}! The answer will be sent to the mail {mail}. Access Date: {access_date}"

    return template("index.tpl", msg=message, year=datetime.now().year)