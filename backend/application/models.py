from application import db

class Trainers(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    first_name = db.Column(db.String(50), nullable=False)
    last_name = db.Column(db.String(50), nullable=False)

    intake_trainers = db.relationship("Intakes",
            secondary="intake_trainers",
            cascade="delete",
            backref=db.backref("trainers"),
            lazy="dynamic"
        )

    def __repr__(self):
        return ''.join([
            'Trainer ID: ', self.id, '\r\n',
            'First Name: ', self.first_name, '\r\n',
            'Last Name: ', self.last_name, '\r\n'
        ])

intake_trainers = db.Table('intake_trainers', db.Model.metadata,
    db.Column('trainer_id', db.Integer, db.ForeignKey('trainers.id')),
    db.Column('intake_id', db.Integer, db.ForeignKey('intakes.id'))
)

class Trainees(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    first_name = db.Column(db.String(50), nullable=False)
    last_name = db.Column(db.String(50), nullable=False)
    intake_id = db.Column(db.Integer, db.ForeignKey("intakes.id"), nullable=False)

    def __repr__(self):
        return ''.join([
            'Trainee ID: ', self.id, '\r\n',
            'First Name: ', self.first_name, '\r\n',
            'Last Name: ', self.last_name, '\r\n',
            'Intake ID: ', self.intake_id, '\r\n'
        ])

class Intakes(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(50), nullable=False)
    start_date = db.Column(db.Date)

    def __repr__(self):
        return ''.join([
            'Intake ID: ', self.id, '\r\n',
            'Intake Name: ', self.name, '\r\n',
            'Start Date: ', str(self.start_date), '\r\n'
        ])
