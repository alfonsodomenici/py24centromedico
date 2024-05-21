from flask import Flask
from config import configDict

def create_app(configName):
    app = Flask(__name__)
    app.config.from_object(configDict[configName])
    return app