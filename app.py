from flask import Flask, render_template, request
import random
import string

app = Flask(__name__)


def generate_password(length):
    lowerD = string.ascii_lowercase
    upperD = string.ascii_uppercase
    digitD = string.digits
    symbolsD = string.punctuation

    combine = lowerD + upperD + digitD + symbolsD

    password = "".join(random.choices(combine, length))
    return password


@app.route("/", methods=["GET", "POST"])
def home():
    password = ""

    if request.method == "POST":
        length = int(request.form["length"])

        if 1 <= length <= len(string.ascii_letters + string.digits + string.punctuation):
            password = generate_password(length)
        else:
            password = "Invalid password length!"

    return render_template("index.html", password=password)


if __name__ == "__main__":
    app.run(debug=True)