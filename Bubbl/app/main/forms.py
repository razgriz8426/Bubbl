from flask_wtf import Form
from wtforms import StringField, SubmitField, validators



class NameForm(Form):
    name = StringField('What is your name?', [validators.DataRequired()])
    submit = SubmitField('Submit')
