#project/__init__.py

from flask import Flask, jsonify
from flask_debugtoolbar import DebugToolbarExtension

app = Flask(__name__.split('.')[0]) #get just the base name

app.config.from_object('project.config.DevelopmentConfig')


@app.route("/ping", methods=['GET'])
def ping_pong():
    return jsonify({
        'status':'success',
        'message': 'pong!'
        }) 

