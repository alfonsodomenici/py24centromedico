from flask import Flask
from config import configDict
from flask_mysqldb import MySQL

db = MySQL()

def create_app(configName):
    app = Flask(__name__)
    app.config.from_object(configDict[configName])
    
    db.init_app(app)
    
    from .api import api 
    app.register_blueprint(api)
    
    return app