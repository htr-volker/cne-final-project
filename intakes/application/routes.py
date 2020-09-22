from application import app
from flask import jsonify, request
import requests

@app.route('/intakes', methods = ["GET"])
def intakes():
    intakes = requests.get("http://backend:6000/intakes")

    data = { 
        "intakes" : intakes.json()["intakes"]
    }

    return jsonify(data)

@app.route('/intakes/info', methods = ["POST"])
def intake_info():
    intake = request.data.decode('utf-8')
    trainers = requests.post("http://backend:6000/intake/trainers", data=intake)
    trainees = requests.post("http://backend:6000/intake/trainees", data=intake)

    data = { 
        "name" : intake,
        "trainers" : trainers.json()["trainers"],
        "trainees" : trainees.json()["trainees"]
    }

    return jsonify(data)

