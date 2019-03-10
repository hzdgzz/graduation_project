from flask import render_template
from . import Superson


@Superson.route("/")
def index():

    return render_template('index.html')


@Superson.route("/Supersons.html")
def Supersons():
    return render_template('Supersons.html')


