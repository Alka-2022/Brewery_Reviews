# backend/__init__.py
from flask import Flask
from flask_pymongo import PyMongo
from .config import Config

app = Flask(__name__)
app.config.from_object(Config)

# Initialize PyMongo
mongo = PyMongo(app)

# Import your routes after initializing the app
from .app import routes
