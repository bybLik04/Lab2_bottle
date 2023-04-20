import re
from bottle import post, request, template
from datetime import datetime
import pdb
import json

questions = {}  # словарь для хранения почти, имени пользователя и вопроса

@post('/home', method='post')
def my_form():
    mail = request.forms.get('ADRESS')  # получаем значение полей из формы
    username = request.forms.get('USERNAME')
    question = request.forms.get('QUEST')

    if not mail or not username:  # проверяем, что поля 'ADRESS' и 'USERNAME' не пустые
        error_msg = "Please fill in all fields"
        return template("index.tpl", msg=error_msg, year=datetime.now().year)

    email_pattern = r'^[a-zA-Z0-9._]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'  # паттерн для проверки валидности email адреса
    if not re.match(email_pattern, mail):  # проверяем, что введенный email адрес соответствует паттерну
        error_msg = "Invalid email address"
        return template("index.tpl", msg=error_msg, year=datetime.now().year)

    if len(question) <= 3 or question.isdigit():  # проверяем, что вопрос состоит из более 3 символов и не состоит только из чисел
        error_msg = "Question should have more than 3 characters and should not consist of only digits"
        return template("index.tpl", msg=error_msg, year=datetime.now().year)

    access_date = datetime.now().strftime("%Y-%m-%d")  # переменная с текущей датой в формате 'ГГГГ-ММ-ДД' 
    if mail in questions:  # проверяем, есть ли уже вопросы от данного пользователя
        questions[mail][0] = username  # обновляем имя пользователя в словаре
        if question not in questions[mail][1:]:  # проверяем, что такой вопрос еще не был задан пользователем
            questions[mail].append(question)  # добавляем вопрос в список вопросов пользователя
        else:
            error_msg = "This question has already been asked by this user"  # сообщение об ошибке
            return template("index.tpl", msg=error_msg, year=datetime.now().year)  # возвращаем шаблон с сообщением об ошибке
    else:
        questions[mail] = [username, question]  # добавляем нового пользователя и его вопрос в словарь questions

    with open('questions.json', 'w') as json_file:  # открываем файл 'questions.json' для записи
        json.dump(questions, json_file, indent=4)  # записываем содержимое словаря в файл


    success_msg = f"Thanks, {username}! The answer will be sent to the mail {mail}. Access Date: {access_date}"
    return template("index.tpl", msg=success_msg, year=datetime.now().year)   # возвращаем шаблон с сообщением
