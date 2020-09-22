from application import db

class Tickets(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    title = db.Column(db.String(50), nullable=False)
    author = db.Column(db.String(50), nullable=False)
    description = db.Column(db.String(500), nullable=False)
    time_created = db.Column(db.DateTime, nullable=False)
    open = db.Column(db.Boolean, nullable=False)

    def __repr__(self):
        return f'''
            Ticket ID: {str(self.id)}\n
            Title: {self.title}\n
            Author: {self.author}\n
            Description: {self.description}\n
            Time Created: {str(self.time_created)}
            Open?: {str(self.open)}
        '''
