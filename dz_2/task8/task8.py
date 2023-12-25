# Создать страницу, на которой будет форма для ввода имени и кнопка "Отправить"
# При нажатии на кнопку будет произведено перенаправление на страницу с flash сообщением, где будет
# выведено "Привет, {имя}!".

from flask import Flask, request, render_template, flash, redirect, url_for
from markupsafe import escape
app = Flask(__name__)
app.secret_key = 'secret_key_flask'


@app.route('/')
def index():
    return render_template('index.html')


# @app.get('/submit')
# def submit_get():
#     return render_template('form.html')
#
#
# @app.post('/submit')
# def submit_post():
#     name = request.form.get('name')
#     return f'Привет, {escape(name)}!'


@app.post('/')
def index_post():
    name = request.form['user_name']
    if name:
        flash(f'Привет, {escape(name)}!', 'success')
        return redirect(url_for('index'))
    else:
        flash(f'Запипишите своё имя', 'danger')
        return redirect(url_for('index'))


if __name__ == '__main__':
    app.run(debug=True)
