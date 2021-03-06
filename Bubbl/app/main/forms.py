from flask_wtf import Form
from wtforms import BooleanField, StringField, SubmitField, validators, TextField, TextAreaField, SubmitField, ValidationError, PasswordField
from ..models import User, db
from flask_pagedown.fields import PageDownField

class NameForm(Form):
    name = StringField('What is your name?', [validators.DataRequired()])
    submit = SubmitField('Submit')


class SignupForm(Form):
    firstname = TextField("First name", [validators.Required("Please enter your first name.")])
    lastname = TextField("Last name",  [validators.Required("Please enter your last name.")])
    email = TextField("Email",  [validators.Required("Please enter your email address."), validators.Email("Please enter a valid email address.")])
    password = PasswordField('Password', [validators.Required("Please enter a password.")])
    submit = SubmitField("Create account")
    username = TextField("Username", [validators.Required("Please enter a username.")])

    def __init__(self, *args, **kwargs):
        Form.__init__(self, *args, **kwargs)

    def validate(self):
        if not Form.validate(self):
            return False

        user = User.query.filter_by(email = self.email.data.lower()).first()
        username = User.query.filter_by(username = self.username.data.lower()).first()
        if user:
            self.email.errors.append("That email already exists.")
            return False
        elif username:
            self.username.errors.append("That username already exists.")
            return False
        else:
            return True


class SigninForm(Form):
  email = TextField("Email",  [validators.Required("Please enter your email address."), validators.Email("Please enter a valid email address.")])
  password = PasswordField('Password', [validators.Required("Please enter a password.")])
  remember_me = BooleanField('Keep me logged in')
  submit = SubmitField("Sign In")
   
  def __init__(self, *args, **kwargs):
    Form.__init__(self, *args, **kwargs)
 
  def validate(self):
    if not Form.validate(self):
      return False
     
    user = User.query.filter_by(email = self.email.data.lower()).first()
    if user and user.check_password(self.password.data):
      return True
    else:
      self.email.errors.append("Invalid e-mail or password")
      return False



class PostForm(Form):
    title = TextField('Title', [validators.Required("Please enter a title")])
    body = PageDownField('Body', [validators.Required("Your blog is empty!")])
    submit = SubmitField('Submit')