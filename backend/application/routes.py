from application import app
from flask import request, jsonify
import requests
from temp_data import data

@app.route('/trainers', methods = ["GET"])
def home():
    return jsonify(data["trainers"])

@app.route('/trainees', methods = ["GET"])
def home():
    return jsonify(data["trainees"])

@app.route('/intakes', methods = ["GET"])
def home():
    return jsonify(data["intakes"])

@app.route('/issues', methods = ["GET"])
def home(): 
    return jsonify(data["issues"])
