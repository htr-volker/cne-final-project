from application import app
from flask import render_template
import requests

def save_page(contents, filename):
    with open(f"templates/{filename}", "w") as page:
        page.write(contents)

@app.route('/', methods = ["GET"])
def home():
    return render_template('home.html', title = 'Home')

@app.route('/trainers', methods = ["GET"])
def trainers():
    page = requests.get("http://trainers:5500/trainers")
    save_page(page.json()["contents"], page.json()["filename"])
    return render_template(page.json()["filename"], title = "Trainers", trainers = page.json()["trainers"])
