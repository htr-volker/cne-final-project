from application import app, db
from application.models import Trainers, Trainees, intakes
from flask import request, jsonify
from application.temp_data import data

@app.route('/trainers', methods = ["GET"])
def trainers():
    trainers = Trainers.query.all()
    return jsonify(trainers)

@app.route('/trainees', methods = ["GET"])
def trainees():
    trainees = Trainees.query.all()
    return jsonify(trainees)

@app.route('/intakes', methods = ["GET"])
def intakes():
    intakes = Intakes.query.all()
    return jsonify(intakes)
