from application import app, db
from application.models import Trainers, Trainees, Intakes
from flask import request, jsonify
from application.temp_data import data

@app.route('/intakes', methods = ["GET"])
def intakes():
    intakes = Intakes.query.all()

    response = { "intakes" : [] }
    
    for intake in intakes:
        intake_json = {
            "id" : intake.id,
            "name" : intake.name,
            "start_date" : intake.start_date
        }
        response["intakes"].append(intake_json)
    
    return jsonify(response)

@app.route('/intake/trainers', methods = ["POST"])
def intake_trainers():
    intake_name = request.data.decode("utf-8")

    trainer_intake = Intakes.query.filter_by(name=intake_name).first()
    trainers = trainer_intake.trainers

    response = { "trainers" : [] }
    
    for trainer in trainers:
        trainer_json = {
            "id" : trainer.id,
            "first_name" : trainer.first_name,
            "last_name" : trainer.last_name
        }
        response["trainers"].append(trainer_json)

    return jsonify(response)

@app.route('/intake/trainees', methods = ["POST"])
def intake_trainees():
    intake_name = request.data.decode("utf-8")
    
    intake = Intakes.query.filter_by(name=intake_name).first()

    trainees = Trainees.query.filter_by(intake_id=intake.id).all()

    response = { "trainees" : [] }
    
    for trainee in trainees:
        trainee_json = {
            "id" : trainee.id,
            "first_name" : trainee.first_name,
            "last_name" : trainee.last_name
        }
        response["trainees"].append(trainee_json)

    return jsonify(response)

@app.route('/trainers', methods = ["GET"])
def trainers():
    trainers = Trainers.query.all()
    
    response = { "trainers" : [] }
    
    for trainer in trainers:
        trainer_json = {
            "id" : trainer.id,
            "first_name" : trainer.first_name,
            "last_name" : trainer.last_name
        }
        response["trainers"].append(trainer_json)
    
    return jsonify(response)

@app.route('/trainees', methods = ["GET"])
def trainees():
    trainees = Trainees.query.all()
    return jsonify(trainees.__dict__)

