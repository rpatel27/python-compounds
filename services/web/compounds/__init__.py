from flask import Flask, render_template, send_from_directory

from .model import db, Compound

app = Flask(__name__)

app.config.from_object("compounds.config.Config")
db.init_app(app)


@app.route("/static/<path:filename>")
def staticfiles(filename):
    return send_from_directory(app.config["STATIC_FOLDER"], filename)


@app.route('/', methods=["GET"])
def main_page():
    return render_template("main.html", compounds=Compound.query.all())