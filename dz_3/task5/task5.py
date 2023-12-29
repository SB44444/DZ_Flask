"""Задание №5
📌 Создать форму регистрации для пользователя.
📌 Форма должна содержать поля: имя, электронная почта, пароль (с подтверждением), дата рождения, согласие на
обработку персональных данных.
📌 Валидация должна проверять, что все поля заполнены корректно (например, дата рождения должна быть в формате дд.мм.гггг).
📌 При успешной регистрации пользователь должен быть перенаправлен на страницу подтверждения регистрации."""

from flask import Flask, render_template, request, redirect, flash, url_for
from model_reg2 import RegistrationForm2
from flask_wtf import CSRFProtect
from models import db, User2


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db_4.db'
app.config['SECRET_KEY'] = 'kkkkkrjrrjjjjjjjjjjjufuuuuu33d92jjj11111111uuu77777775'
db.init_app(app)
csrf = CSRFProtect(app)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/registration2/', methods=['GET', 'POST'])
def registration2():
    form = RegistrationForm2()
    if request.method == 'POST' and form.validate():
        name = form.name.data.lower()
        surname = form.surname.data.lower()
        email = form.email.data
        user = User2(name=name, surname=surname, email=email)
        if User2.query.filter(User2.email == email).first():
            flash(f'Пользователь с таким e-mail {email} уже зарегистрирован')
            return redirect(url_for('registration'))
        user.set_password(form.password.data)
        db.session.add(user)
        db.session.commit()
        flash(f'Пользователь зарегистрирован')
        return redirect(url_for('registration2'))
    return render_template('registration2.html', form=form)


@app.cli.command('db-init')
def db_init():
    db.create_all()
    print('sucsess, db сreated')
