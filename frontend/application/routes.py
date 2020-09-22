from application import app
from flask import render_template
import requests

@app.route('/', methods = ["GET"])
def home():
    return render_template('home.html', title = 'Home')

@app.route('/trainers', methods = ["GET"])
def trainers():
    trainers = requests.get("http://trainers:5500/trainers")
    app.logger.info(trainers.json())
    return render_template("trainers.html", title = "Trainers", trainers = trainers.json())

@app.route('/intakes', methods = ["GET"])
def intakes():
    intakes = requests.get("http://intakes:5501/intakes")
    app.logger.info(intakes.json())
    return render_template("intakes.html", title = "Intakes", intakes = intakes.json())

@app.route('/intakes/<intake>', methods = ["GET"])
def intake_info(intake):
    intake_info = requests.post("http://intakes:5501/intakes/info", data = intake)
    app.logger.info(intake_info.json())
    return render_template("intake_info.html", title = intake_info.json()["name"], intake = intake_info.json())