from flask import Flask

app = Flask(__name__)


@app.route("/")
def hello_world():
    return 'Hello, World!'


@app.route("/hii")
def say_hii():
    return 'Hii!'


if __name__ == "__main__":
    app.run()

