from flask_wtf import Form
from wtforms import StringField, SubmitField, validators, TextField, TextAreaField, SubmitField, ValidationError, PasswordField
from .. import db
from ..models import User

class NameForm(Form):
    name = StringField('What is your name?', [validators.DataRequired()])
    submit = SubmitField('Submit')


class SignupForm(Form):
    firstname = TextField("First name", [validators.Required("Please enter your first name.")])
    lastname = TextField("Last name",  [validators.Required("Please enter your last name.")])
    email = TextField("Email",  [validators.Required("Please enter your email address."), validators.Email("Please enter your email address.")])
    password = PasswordField('Password', [validators.Required("Please enter a password.")])
    submit = SubmitField("Create account")

    def __init__(self, *args, **kwargs):
        Form.__init__(self, *args, **kwargs)

    def validate(self):
        if not Form.validate(self):
            return False

        user = User.query.filter_by(email = self.email.data.lower()).first()
        if user:
            self.email.errors.append("That email already exists.")
            return False
        else:
            return True