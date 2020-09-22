from application import app, db
from application.models import Tickets
from flask import request, jsonify
from datetime import datetime

@app.route('/open', methods = ["GET"])
def open_tickets():
    tickets = Tickets.query.filter_by(open=True).all()

    response = { "tickets" : [] }
    
    for ticket in tickets:
        ticket_json = {
            "id" : ticket.id,
            "title" : ticket.title,
            "author" : ticket.author,
            "description" : ticket.description,
            "time_created" : ticket.time_created,
            "open" : ticket.open
        }
        response["tickets"].append(ticket_json)
    
    return jsonify(response)

@app.route('/closed', methods = ["GET"])
def closed_tickets():
    tickets = Tickets.query.filter_by(open=False).all()

    response = { "tickets" : [] }
    
    for ticket in tickets:
        ticket_json = {
            "id" : ticket.id,
            "title" : ticket.title,
            "author" : ticket.author,
            "description" : ticket.description,
            "time_created" : ticket.time_created,
            "open" : ticket.open
        }
        response["tickets"].append(ticket_json)
    
    return jsonify(response)

@app.route('/create', methods = ["POST"])
def create_ticket():
    new_ticket = request.get_json()
    
    db.session.add(
        Tickets(
            title = new_ticket["title"],
            author = new_ticket["author"],
            description = new_ticket["description"],
            time_created = datetime.strptime(new_ticket["time_created"], '%Y-%m-%d %H:%M:%S.%f'),
            open = True
        )
    )

    db.session.commit()
    return "Ticket Added to Queue"

@app.route('/close', methods = ["POST"])
def close_ticket():
    ticket_id = request.data.decode("utf-8")
    ticket = Ticket.query.filter_by(id = ticket_id).first()
    ticket.open = False
    db.session.commit()
    return f"Ticket {ticket_id} closed"

@app.route('/update', methods = ["GET"])
def update_ticket():
    return "WIP"

@app.route('/delete', methods = ["GET"])
def delete_ticket():
    return "WIP"