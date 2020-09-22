from application import app
from application.forms import CreateTicketForm
from flask import render_template, request, redirect, url_for
from datetime import datetime
import requests

@app.route('/', methods = ["GET"])
def home():
    return render_template('home.html', title = 'Home')

@app.route('/queue', methods = ["GET"])
def queue():
    open_tickets = requests.get("http://gateway:6000/tickets/open")
    closed_tickets = requests.get("http://gateway:6000/tickets/closed")
    
    app.logger.info(open_tickets.json())
    app.logger.info(closed_tickets.json())
    
    return render_template("queue.html",
        title = "Help Queue",
        open_tickets = open_tickets.json(),
        closed_tickets = closed_tickets.json()
    )

@app.route('/create', methods = ["GET", "POST"])
def create_ticket():
    form = CreateTicketForm()
    
    if form.validate_on_submit():
        ticket = { 
            "title" : form.title.data,
            "author" : form.author.data,
            "description" : form.description.data,
            "time_created" : str(datetime.now())
        }     
        requests.post("http://gateway:6000/tickets/create", json = ticket)
        return redirect(url_for("queue"))
    
    return render_template("create_ticket.html",
        title = "Create Ticket",
        form = form
    )

@app.route('/close/<int:id>', methods = ["GET"])
def close_ticket(id):
    requests.post("http://gateway:6000/tickets/close", data = str(id))
    return redirect(url_for("queue"))

'''
@app.route('/intakes', methods = ["GET"])
def intakes():
    intakes = requests.get("http://intakes:5501/intakes")
    app.logger.info(intakes.json())
    
    return render_template("intakes.html",
        title = "Intakes",
        intakes = intakes.json()
    )

@app.route('/intakes/<intake>', methods = ["GET"])
def intake_info(intake):
    intake_info = requests.post("http://intakes:5501/intakes/info", data = intake)
    app.logger.info(intake_info.json())
    
    return render_template("intake_info.html",
        title = intake_info.json()["name"],
        intake = intake_info.json()
    )
'''