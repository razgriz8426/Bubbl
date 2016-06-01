"""
Routes and views for the flask application.
"""

from datetime import datetime
from flask import render_template
from Bubbl import app

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
