"""
Routes and views for the flask application.
"""


from datetime import datetime
from flask import render_template, request, session, redirect, url_for, flash
from app import app
from wtforms import StringField, SubmitField, validators, Form
from .forms import NameForm, SignupForm, SigninForm
from . import main

from flask_bootstrap import Bootstrap





@main.route('/')
@main.route('/index.html')
@main.route('/home.html')
def home():
    """Renders the home page."""
    return render_template(
        'index.html',
        title='Bubbl Baby!!!',
    )

@main.route('/layout')
def layout():
    """Renders the layout page."""
    return render_template(
        'layout.html',
        title='Bubbl Baby!!!',
    )

@main.route('/contact')
@main.route('/contact.html')
def contact():
    """Renders the contact page."""
    return render_template(
        'contact.html',
        title='Contact',
        year=datetime.now().year,
        message='Bubbl Inc. (maybe...)'
    )

@main.route('/about.html')
@main.route('/about')
def about():
    """Renders the about page."""
    return render_template(
        'about.html',
        title='About Bubbl',
        year=datetime.now().year,
        message='See homepage for anything relevant'
    )

@main.route('/boot')
def boot():
    return render_template(
        'boot.html',
        title='Bootstrap?'
        )

@main.route('/test', methods=['GET', 'POST'])
def test():
    form = NameForm()
    if form.validate_on_submit():
        user = Test(name = form.name.data)
        db.session.add(user)
        session['name'] = form.name.data
        form.name.data = ''
        return redirect(url_for('main.test'))
    return render_template('test.html',
        form = form, name = session.get('name'),
        known = session.get('known', False))

@main.route('/user/<name>')
def user(name):
    return render_template(
        'user.html',
        name=name
    )



@main.route('/testdb')
def testdb():
    if db.session.query("1").from_statement("SELECT 1").all():
        return 'It works.'
    else:
        return 'Fuck.'

@main.route('/form', methods=['GET', 'POST'])
def form():
    form = NameForm()
    if form.validate_on_submit():
        old_name = session.get('name')
        if old_name is not None and old_name != form.name.data:
            flash('Looks like you have changed your name!')
        session['name'] = form.name.data
        session['message'] = ''
        form.name.data = ''
        return redirect('/form')
    elif request.method == 'POST':
        session['message'] = 'Please enter a name'
        session['name'] = None
        return redirect('/form')
    return render_template('form.html', form=form, name=session.get('name'), message=session.get('message'))


@main.route('/signup', methods=['GET', 'POST'])
def signup():
    form = SignupForm()

    if request.method == 'POST':
        if form.validate() == False:
            return render_template('signup.html', form=form)
        else: 
       #     newuser = User(form.firstname.data, form.lastname.data, form.email.data, form.password.data)
        
            firstname=request.form['firstname']
            lastname=request.form['lastname']
            email=request.form['email']
            password=request.form['password']
            try:
                with connection.cursor() as cursor:
                    sql = "INSERT INTO users (firstname,lastname,email,password) VALUES (%s, %s, %s, %s)"
                    curson.execute(sql, (firstname, lastname, email, password))
                    connection.commit()
            finally:
                connection.close()
                return redirect(url_for('main.profile'))

    elif request.method =='GET':
        return render_template('signup.html', form=form)


@main.route('/profile')
def profile(): 

    if 'email' not in session:
        return redirect(url_for('main.signin'))

    user = User.query.filter_by(email = session['email']).first()

    if user is None:
        return redirect(url_for('main.signin'))
    else:
        return render_template('profile.html')


@main.route('/signin', methods=['GET', 'POST'])
def signin():
  form = SigninForm()
   
  if request.method == 'POST':
    if form.validate() == False:
      return render_template('signin.html', form=form)
    else:
      session['email'] = form.email.data
      return redirect(url_for('main.profile'))
                 
  elif request.method == 'GET':
    return render_template('signin.html', form=form)

@main.route("/Authenticate")
def Authenticate():
    username = request.args.get('UserName')
    password = request.args.get('Password')
    cursor = mysql.connect().cursor()
    cursor.execute("SELECT * from User where Username='" + username + "' and Password='" + password + "'")
    data = cursor.fetchone()
    if data is None:
        return "Username or Password is wrong"
    else:
        return "Logged in successfully"