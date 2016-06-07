"""
The flask application package.
"""

from flask import Flask
app = Flask(__name__)
app.config['SECRET_KEY'] = 'Razgriz8426?secretkey'


import Bubbl.views
