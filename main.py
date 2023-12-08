from flask import Flask, render_template

PORTFOLIO_PERSON_NAME = "John M. Caldwell, Jr"

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("index.html", PORTFOLIO_PERSON_NAME=PORTFOLIO_PERSON_NAME)


@app.route("/bye/<name>/")
def bye():
    pass


if __name__ == '__main__':
    app.run(debug=True)
