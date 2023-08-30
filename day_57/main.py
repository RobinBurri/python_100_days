from flask import Flask, render_template
from helper import find_ages, find_genders

app = Flask(__name__)


@app.route("/<name>")
def hello(name):
    age = find_ages(name)
    gender = find_genders(name)
    return render_template("index.html", name=name, age=age, gender=gender)


if __name__ == "__main__":
    app.run(debug=True, host="127.0.0.1", port=8080)
