# Создать страницу, на которой будет форма для ввода имени и возраста пользователя и кнопка "Отправить".
# При нажатии на кнопку будет произведена проверка возраста и переход на страницу с результатом или на
# страницу с ошибкой в случае некорректного возраста.

from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.post('/validation/')
def verification():
    name = request.form.get('name').title()
    age = request.form.get('age')
    try:
        if int(age) >= 18:
            return render_template('pass_age.html', name=name, age=age)
        else:
            return render_template('stop_age.html', age=int(age))
    except ValueError:
        return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True)
