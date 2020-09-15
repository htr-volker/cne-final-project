from application import app
from flask import request, jsonify
import requests

@app.route('/trainers', methods = ["GET"])
def home():
    
    return jsonify(trainers)

@app.route('/trainees', methods = ["GET"])
def home():
    
    return jsonify(trainees)

@app.route('/intakes', methods = ["GET"])
def home():
    
    return jsonify(intakes)

@app.route('/issues', methods = ["GET"])
def home():
    
    return jsonify(issues)
