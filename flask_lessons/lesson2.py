# Сделать шаблон своего сайта в Figma
# Для проекта "Парсинг пиццерий" для страницы регистрации сделать обработку 
# методов GET и POST:
    # Если метод GET вывести в консоль сообщение
    # Если метод POST вывести в консоль все данные которые вписал пользователь


from flask import Flask, render_template, request, redirect, url_for
from random import randint

app = Flask(__name__)


@app.route("/", methods=['GET', 'POST'])
def index_page():
    if request.method == 'GET':
        print('GET')
        # user = request.args.get('nm')
        # print(f'Args: {user}')
    elif request.method == 'POST':
        print('POST')
        user = request.form['nm']
        print(f'Username: {user}')
        return redirect(url_for('user_profile', username=user))
    else:
        print('another metods')

    number_str = str(randint(0, 100))
    title = f'Hello {number_str}'
    return render_template('index.html', title=title)


@app.route("/choice_brand")
def choice_brand():
    number_str = str(randint(0, 100))
    title = f'Hello {number_str}'
    return render_template('choice_brand.html', title=title)


@app.route("/user/<username>")
def user_profile(username):
    number_str = str(randint(0, 100))
    title = f'Hello {number_str}'
    return render_template('user_profile.html', title=title, username=username)


if __name__ == "__main__":
    app.run(debug=True)