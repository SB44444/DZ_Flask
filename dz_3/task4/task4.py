"""Задание №4
📌 Создайте форму регистрации пользователя с использованием Flask-WTF. Форма должна содержать следующие поля:
○ Имя пользователя (обязательное поле)
○ Электронная почта (обязательное поле, с валидацией на корректность ввода email)
○ Пароль (обязательное поле, с валидацией на минимальную длину пароля)
○ Подтверждение пароля (обязательное поле, с валидацией на совпадение с паролем)
📌 После отправки формы данные должны сохраняться в базе данных (можно использовать SQLite)
и выводиться сообщение об успешной регистрации. Если какое-то из обязательных полей не
заполнено или данные не прошли валидацию, то должно выводиться соответствующее
сообщение об ошибке.
📌 Дополнительно: добавьте проверку на уникальность имени пользователя и электронной почты в
базе данных. Если такой пользователь уже зарегистрирован, то должно выводиться сообщение
об ошибке."""

from flask import Flask, render_template, request, redirect
from model_reg1 import db, Users
from flask_wtf import CSRFProtect
from model_form import RegistrationForm

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db_4.db'
app.config['SECRET_KEY'] = 'kkkkkrjrrjjjjjjjjjjjufuuuuu33d92jjj11111111uuu77777775'
db.init_app(app)
csrf = CSRFProtect(app)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/registration/', methods=['GET', 'POST'])
def registration():
    form = RegistrationForm()
    if request.method == 'POST' and form.validate():
        username = str(form.username.data)
        password = str(form.password.data)
        email = str(form.email.data)
        print(f'{username= }, {password= }, {email= }')
        user = Users(username=username, password=password, email=email)
        db.session.add(user)
        db.session.commit()
        print(f'Пользователь зарегистрирован')
        return redirect('/')
    return render_template('registration.html', form=form)


@app.cli.command('db-init')
def db_init():
    db.create_all()
    print('sucsess, db сreated')
