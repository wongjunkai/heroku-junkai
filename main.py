from flask import Flask, redirect, url_for, request, render_template

app = Flask(__name__)


@app.route('/')
def hello_world():
    return render_template('test.html')


if __name__ == '__main__':
    app.run(port='80')