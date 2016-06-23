"""
Routes and views for the flask application.
"""

import os
from datetime import datetime
from flask import Flask,render_template, request, session, redirect, url_for, flash
from . import main
from .. import db
from ..models import User
from wtforms import StringField, SubmitField, validators, Form
from .forms import NameForm

from flask_sqlalchemy import SQLAlchemy
from flask_bootstrap import Bootstrap


app = Flask(__name__)

bootstrap = Bootstrap(app)


app.config['SECRET_KEY'] = 'Razgriz8426?secretkey'
app.secret_key = 'Razgriz8426?secretkey'

#database information

SQLALCHEMY_DATABASE_URL = 'mysql://apps:Razgriz8426?mysql@localhost/apps'
SQLALCHEMY_COMMIT_ON_TEARDOWN = True
SQLALCHEMY_TRACK_MODIFICATIONS = False
db = SQLAlchemy(app)


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

@main.route('/test')
def test():
    """Renders the test page."""
    return render_template(
        'test.html',
        title='Tests Here',
       year=datetime.now().year,
       message='This is a test template!'
    )

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

