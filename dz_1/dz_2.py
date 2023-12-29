"""
Задание 2.
Создать базовый шаблон для интернет-магазина, содержащий общие элементы дизайна (шапка, меню, подвал),
и дочерние шаблоны для страниц категорий товаров и отдельных товаров.
Например: страницы "Одежда", "Обувь" и "Куртка", используя базовый шаблон
"""
from flask import Flask
from flask import render_template

app = Flask(__name__)


@app.route('/')
@app.route('/index/')
def index():
    category = [
        {"title": 'Одежда', "func_name": 'dress'},
        {"title": 'Обувь', "func_name": 'shoes'},
        {"title": 'Игрушки', "func_name": 'toys'}
    ]
    return render_template('store_index.html', category=category)


@app.route('/dress/')
def dress():
    return render_template('store_dress.html')


@app.route('/shoes/')
def shoes():
    return render_template('store_shoes.html')


@app.route('/toys/')
def toys():
    return render_template('store_toys.html')


if __name__ == "__main__":
    app.run(debug=True)
