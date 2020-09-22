from application import app
from flask import jsonify, request
import requests

@app.route('/trainers', methods = ["GET"])
def trainers():
    trainers = requests.get("http://backend:6000/trainers")

    data = { 
        "trainers" : trainers.json()["trainers"]
    }

    return jsonify(data)
