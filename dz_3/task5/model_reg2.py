"""Задание №5.
Создать форму регистрации для пользователя. Форма должна содержать поля: имя, электронная почта, пароль (с подтверждением),
дата рождения, согласие на обработку персональных данных. Валидация должна проверять, что все поля заполнены корректно
(например, дата рождения должна быть в формате дд.мм.гггг). При успешной регистрации пользователь должен быть перенаправлен
 на страницу подтверждения регистрации."""


from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import DataRequired, Email, Length, EqualTo


class RegistrationForm2(FlaskForm):
    name = StringField('Name', validators=[DataRequired()])
    surname = StringField('Surname', validators=[DataRequired()])
    email = StringField('E-mail', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired(), Length(min=6)])
    confirm_password = PasswordField('Confirm Password', validators=[DataRequired(), EqualTo('password')])
    check = BooleanField('Сonsent to the processing of user data', validators=[DataRequired()])
    submit = SubmitField('Sign In')
