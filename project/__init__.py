#project/__init__.py

import os
import datetime
from flask import Flask, jsonify
from flask_debugtoolbar import DebugToolbarExtension
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__.split('.')[0]) #get just the base name

app_settings = os.getenv('APP_SETTINGS')
app.config.from_object('project.config.DevelopmentConfig')


@app.route("/ping", methods=['GET'])
def ping_pong():
    return jsonify({
        'status':'success',
        'message': 'pong!'
        }) 

