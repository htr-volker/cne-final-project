from application import app
from flask import jsonify
import requests

@app.route('/trainers', methods = ["GET"])
def trainers():
    trainers = requests.get("http://backend:6000/trainers")

    with open("application/templates/trainers.html", "r") as file:
        contents = file.read()

    data = { 
            "filename" : "application/templates/trainers.html",
            "contents" : contents,
            "variables" : trainers
            }

    return jsonify(data)
