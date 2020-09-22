from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from os import getenv

app = Flask(__name__)

user = getenv("MYSQL_USER")
password = getenv("MYSQL_ROOT_PASSWORD")

app.config["SQLALCHEMY_DATABASE_URI"] = f"mysql+pymysql://root:{password}@database:3306/helpqueue"

db = SQLAlchemy(app)

from application import routes