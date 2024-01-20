from flask import Flask, render_template, request, redirect, url_for
from random import randint
from flask_login import LoginManager
from flask_bcrypt import Bcrypt


app = Flask(__name__)
bcrypt = Bcrypt(app)

login_manager = LoginManager()
login_manager.init_app(app)

# login 
# password


class User:
    def __init__(self, login, password='0000'):
        self.login = login
        self.password = password
        self.id = 0

user1 = User(login='demo', password='1111')


@login_manager.user_loader
def loader_user(user_id):
    return user1
    # return Users.query.get(user_id)


def login():
    content = {}

    if request.method == 'POST':
        correct_password = '1234'
        correct_username = 'user1'

        print('POST')
        username = request.form['username']
        password = request.form['password']
        print(f'Username: {username} Password: {password}')

        if username == correct_username and password == correct_password:
            return redirect(url_for('user_profile', username=username))
        else:
            content['error_keypare'] = 'Логин и пароль не корректны!'
            return render_template('login.html', content=content)
    elif request.method == 'GET':
        return render_template('login.html', content=content)


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

    password = 'asdfg_asdf_asdf'
    hashed_password = bcrypt.generate_password_hash(password).decode('utf-8')
    is_valid = bcrypt.check_password_hash(hashed_password, password)
    print(is_valid)

    content = {
        'title': title,
        'cities': cities, 
        'person': person, 
        'checkbox': checkbox,
        'password': password,
        'hashed_password': hashed_password
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

# Добавление URL страниц
app.add_url_rule("/", 'index_page', index_page, methods=['GET', 'POST'])
app.add_url_rule("/choice_brand", 'choice_brand', choice_brand)
app.add_url_rule("/user/<string:username>", 'user_profile', user_profile)
app.add_url_rule("/login", 'login', login, methods=['GET', 'POST'])


if __name__ == "__main__":

    app.run(debug=True)

# Bcrypt

