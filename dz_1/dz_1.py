"""
Задание 1
# Написать функцию, которая будет выводить на экран HTML страницу с блоками новостей.
# Каждый блок должен содержать заголовок новости, краткое описание и дату публикации.
# Данные о новостях должны быть переданы в шаблон через контекст
"""

from flask import Flask
from flask import render_template


app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/news/')
def news():
    context = [{
        'day': 'Сегодня',
        'title': 'Музыкальный театр',
        'data': 'На выходных Музыкальный театр Ростова представит праздничный концерт «Мелодии Новогодней ночи». \
            Артисты театра покажут 30 номеров из опер, балетов, оперетт и мюзиклов'
        },
        {
        'day': 'Вчера',
        'title': 'Мозаичные подземные переходы',
        'data': 'Комитет по охране объектов культурного наследия Ростовской области не утвердил проект реставрации четырех подземных переходов \
            с мозаичными панно в центре Ростова-на-Дону'
        },
        {
        'day': 'Ранее',
        'title': 'Набережная Дона',
        'data': 'Ростовский порт перенесут на левый берег Дона на год ранее изначально планируемого срока — к концу 2024 года. \
            Это откроет масштабные перспективы для преображения города.'
        }
    ]
    return render_template('news.html', news=context)


if __name__ == '__main__':
    app.run(debug=True)
