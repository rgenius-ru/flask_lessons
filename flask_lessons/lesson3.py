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
    return render_template('index.html', title=title)


def choice_brand():
    number_str = str(randint(0, 100))
    title = f'Hello {number_str}'
    return render_template('choice_brand.html', title=title)


def user_profile(username):
    number_str = str(randint(0, 100))
    title = f'Hello {number_str}'
    return render_template('user_profile.html', title=title, username=username)

# Синтаксис:
# add_url_rule(<url rule>, <endpoint>, <view function>) 

app.add_url_rule("/", 'index_page', index_page, methods=['GET', 'POST'])
app.add_url_rule("/choice_brand", 'choice_brand', choice_brand)
app.add_url_rule("/user/<string:username>", 'user_profile', user_profile)

# Пример конверторов типов в адресе:
# app.add_url_rule("/user_id/<int:id>", 'user_profile', user_profile)

# string - любые символы кроме "/"
# int
# float
# path - тоже что и string, но поддерживается и "/"
# uuid 454df-df453-...
# any


# HTTP Коды редиректа:
# Code 	

# Status
# 300 	Multiple_choices
# 301 	Moved_permanently
# 302 	Found
# 303 	See_other
# 304 	Not_modified
# 305 	Use_proxy
# 306 	Reserved
# 307 	Temporary_redirect

if __name__ == "__main__":
    app.run(debug=True)
