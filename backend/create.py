from application import db
from application.models import Trainers, Trainees, Intakes
from datetime import date

db.drop_all()
db.create_all()

trainer1 = Trainers(first_name="Bill S.", last_name="Preston, Esq.")
trainer2 = Trainers(first_name="Ted 'Theodore'", last_name="Logan")

trainee1 = Trainees(first_name="Thea", last_name="Preston")
trainee2 = Trainees(first_name="Billie",last_name="Logan")

intake = Intake(name="SeptDevOps", start_date=date(2020, 9, 14))
intake.trainers.append(trainer1)
intake.trainers.append(trainer2)

objects = [
    trainer1, trainer2, trainee1, trainee2, intake
]

db.session.add_all(objects)
db.session.commit()
