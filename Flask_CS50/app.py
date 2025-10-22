from flask import Flask, render_template, request

app = Flask(__name__)


@app.route("/")
def index():
    return render_template(template_name_or_list="index.html")

@app.route(rule="/greet", methods=["POST"])
def greet():
    # name = request.args.get("name", "world")
    name = request.form.get("name", "world")
    return render_template(template_name_or_list="greet.html", name=name)
