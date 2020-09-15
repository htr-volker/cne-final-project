from application import app
from flask import jsonify
import requests

@app.route('/trainers', methods = ["GET"])
def trainers():
    trainers = requests.get("http://backend:6000/trainers")

    with open("trainers.html", "r") as file:
        contents = read(file)

    data = { 
            "filename" : "templates/trainers.html",
            "contents" : contents,
            "variables" : trainers
            }

    return jsonify(data)
