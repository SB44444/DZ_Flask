from flask import Flask


app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello World!'

"""Условие __name__ == '__main__' означает, что сервер работает
только в том случае, если скрипт выполняется непосредственно из
Python-интерпретатора и не используется в качестве импортированного модуля.
"""
if __name__ == '__main__':
    app.run()
    