# Django vs Flask

# ДЗ почитать про html и css

from flask import Flask, render_template
from random import randint


app = Flask(__name__)


@app.route("/")
def world():
    title = 'Hello ' + str(randint(0, 100))
    return render_template('index.html', title=title)


if __name__ == "__main__":
    app.run()
