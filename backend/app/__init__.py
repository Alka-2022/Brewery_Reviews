# backend/app/__init__.py
from flask import Flask
from flask_cors import CORS
from flask_pymongo import PyMongo

app = Flask(__name__)
CORS(app)  # Allow CORS for all routes
app.config.from_object(Config)

mongo = PyMongo(app)
from .app import routes
