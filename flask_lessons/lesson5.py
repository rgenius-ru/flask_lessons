from flask import Flask, render_template, request, redirect, url_for
from random import randint

app = Flask(__name__)


def index_page():
    if request.method == 'GET':
        print('GET')
        # user = request.args.get('name')
        # print(f'Args: {user}')
    elif request.method == 'POST':
        print('POST')
        user = request.form['name']
        print(f'Username: {user}')

        if 'scales1' in request.form:    
            checkbox1 = request.form['scales1']
            print(f'checkbox1: {checkbox1}')
        else:
            print('checkbox1: off')

        return redirect(url_for('user_profile', username=user))
    else:
        print('another metods')

    number_str = str(randint(0, 100))
    title = f'Hello {number_str}'

    cities = {
        'Воронеж':110,
        'Калуга':120,
        'Липецк':130
    }

    person = 'admin'

    checkbox = 5

    content = {
        'title': title,
        'cities': cities, 
        'person': person, 
        'checkbox': checkbox,
    }

    return render_template('index.html', content=content)


def choice_brand():
    number_str = str(randint(0, 100))
    title = f'Hello {number_str}'
    return render_template('choice_brand.html', title=title)


def user_profile(username):
    number_str = str(randint(0, 100))
    title = f'Hello {number_str}'
    return render_template('user_profile.html', title=title, username=username)


app.add_url_rule("/", 'index_page', index_page, methods=['GET', 'POST'])
app.add_url_rule("/choice_brand", 'choice_brand', choice_brand)
app.add_url_rule("/user/<string:username>", 'user_profile', user_profile)



if __name__ == "__main__":
    app.run(debug=True)


# Смена IP и порта

# Через команду оболочки flask
    # set FLASK_APP=app.py
    # flask run
    # flask run --host=192.168.0.105 --port=5000

# Через параметры app.run
    # app.run(host='192.168.1.100', port=8001)
    # app.run(host='0.0.0.0', port=80)