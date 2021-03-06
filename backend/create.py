from application import db
from application.models import Trainers, Trainees, Intakes, intake_trainers
from datetime import date

db.drop_all()
db.create_all()

trainer1 = Trainers(first_name="Bill S.", last_name="Preston, Esq.")
trainer2 = Trainers(first_name="Ted 'Theodore'", last_name="Logan")
trainers = [trainer1, trainer2]
db.session.add_all(trainers)
db.session.commit()

intake = Intakes(name="SeptDevOps", start_date=date(2020, 9, 14))
db.session.add(intake)
db.session.commit()

intake.trainers.append(Trainers.query.filter_by(first_name="Bill S.").first())
intake.trainers.append(Trainers.query.filter_by(first_name="Ted 'Theodore'").first())

trainee1 = Trainees(first_name="Thea", last_name="Preston", intake_id=Intakes.query.filter_by(name="SeptDevOps").first().id)
trainee2 = Trainees(first_name="Billie",last_name="Logan", intake_id=Intakes.query.filter_by(name="SeptDevOps").first().id)
trainees = [trainee1, trainee2]
db.session.add_all(trainees)
db.session.commit()
