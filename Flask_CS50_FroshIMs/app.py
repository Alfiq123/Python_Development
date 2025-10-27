import sqlite3
from flask import Flask, render_template, request

app = Flask(__name__)

SPORTS = [
    "Basketball",
    "Soccer",
    "Ultimate Frisbee"
]

REGISTRANTS = {}


@app.route("/")
def index():
    return render_template(template_name_or_list="index.html", sports=SPORTS)


@app.route(rule="/register", methods=["POST"])
def register():

    name = request.form.get("name")
    if not name:
        return render_template(template_name_or_list="error.html", messege="Missing Name!")

    sport = request.form.get("sport")
    if not sport:
        return render_template(template_name_or_list="error.html", messege="Missing Sport!")
    elif sport not in SPORTS:
        return render_template(template_name_or_list="error.html", messege="Invalid Sport!")

    REGISTRANTS[name] = sport

    return render_template("sucess.html")

@app.route("/registrants")
def registrants():
    return render_template(template_name_or_list="registrants.html", registrants=REGISTRANTS)

    # if not request.form.get("name") or request.form.get("sport") not in SPORTS:
        # return render_template("failure.html")
    # return render_template("sucess.html")
