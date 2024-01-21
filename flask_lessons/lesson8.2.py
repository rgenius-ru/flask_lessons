# 1 Импорт
from flask import Flask, render_template, request, url_for, redirect, flash
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager, UserMixin, login_required, login_user, logout_user

app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///db.sqlite"
app.config["SECRET_KEY"] = "fghfghfgh"  # безопасное сохранение сессий в браузере

db = SQLAlchemy()

login_manager = LoginManager()
login_manager.init_app(app)


# 2 Создание модели User и базы данных
class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(250), nullable=False, unique=True)
    password = db.Column(db.String(250), nullable=False)


db.init_app(app)

with app.app_context():
    db.create_all()


# 3 Добавление user_loader
@login_manager.user_loader
def loader_user(user_id):
    print('================ loader_user ==================')
    return db.session.get(User, user_id)


# 4 Создание страниццы регистрации и функции её обработки
def register():
    if request.method == 'POST':
        user = User(
            username=request.form.get('username'),
            password=request.form.get('password')
        )

        # Проверка что такое имя ещё не зарегистрировано

        db.session.add(user)
        db.session.commit()

        return redirect(url_for('login'))

    return render_template('sign_up_lesson8.2.html')

app.add_url_rule('/register', 'register', register, methods=['GET', 'POST'])


# 5 Создание страницы входа пользователя
def login():
    if request.method == 'POST':
        user = User.query.filter_by(
            username=request.form.get('username')
        ).first()

        if user and user.password == request.form.get('password'):
            login_user(user, remember=True)
            return redirect(url_for('home'))
        
        flash('Не правильная пара логин/пароль')

    return render_template('login_lesson8.2.html')

app.add_url_rule('/login', 'login', login, methods=['GET', 'POST'])


# 6 Создание главное страницы 
def home():
    return render_template('index_lesson8.2.html')

app.add_url_rule('/', 'home', home)


# 7 Добавление функционала разлогирования


# 8 Создание защищённой страницы профиля пользователя
@login_required
def user_profile():
    return render_template('user_profile_lesson8.2.html')

app.add_url_rule('/user_profile', 'user_profile', user_profile)


# Запуск приложения
if __name__ == '__main__':
    app.run(debug=True)