"""
Routes and views for the flask application.
"""

from datetime import datetime
from flask import Flask, render_template, request, session, redirect, url_for, flash
from Bubbl import app
from wtforms import StringField, SubmitField, validators, Form


app.config['SECRET_KEY'] = 'Razgriz8426?secretkey'



class NameForm(Form):
    name = StringField('What is your name?', [validators.InputRequired()])
    submit = SubmitField('Submit')
    name.data = None

@app.route('/')
@app.route('/home')
def home():
    """Renders the home page."""
    return render_template(
        'index.html',
        title='Bubbl Baby!!!',
        year=datetime.now().year,
    )

@app.route('/contact')
def contact():
    """Renders the contact page."""
    return render_template(
        'contact.html',
        title='Contact',
        year=datetime.now().year,
        message='Bubbl Inc. (maybe...)'
    )

@app.route('/about')
def about():
    """Renders the about page."""
    return render_template(
        'about.html',
        title='About Bubbl',
        year=datetime.now().year,
        message='See homepage for anything relevant'
    )

@app.route('/test')
def test():
    """Renders the test page."""
    return render_template(
        'test.html',
        title='Tests Here',
       year=datetime.now().year,
       message='This is a test template!'
    )

@app.route('/user/<name>')
def user(name):
    return render_template(
        'user.html',
        name=name
        
    )

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

@app.errorhandler(500)
def internal_server_error(e):
    return render_template('500.html'), 500


@app.route('/form', methods=['GET', 'POST'])
def form():
    form = NameForm(request.form)
    if form.validate():
        old_name = session.get('name')
        if old_name is not None and old_name != form.name.data:
            flash('Looks like you have changed your name!')
        session['name'] = form.name.data
        session['message'] = ''
        form.name.data = ''
        return redirect(url_for('form'))
    elif request.method == 'POST':
        session['message'] = 'Please enter a name'
        session['name'] = None
        return redirect(url_for('form'))
    return render_template('form.html', form=form, name=session.get('name'), message=session.get('message'))


