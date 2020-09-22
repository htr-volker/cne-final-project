from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, Length, ValidationError

class CreateTicketForm(FlaskForm):
    title = StringField(
        'Title',
        validators = [
            DataRequired(),
            Length(min = 1, max = 30)
        ]
    )
    author = StringField(
        'Author',
        validators = [
            DataRequired(),
            Length(min = 3, max = 30)
        ]
    )
    description = StringField(
        'Description',
        validators = [
            DataRequired(),
            Length(max = 500)
        ]
    )
    submit = SubmitField('Submit Ticket')

class TicketCompletedButton(FlaskForm):
    add_button = SubmitField('Done!')