from flask import Flask, render_template
from os import getenv

app = Flask(__name__)
app.static_folder = 'static'
app.config['SECRET_KEY'] = getenv('SECRET_KEY')

from application import routes