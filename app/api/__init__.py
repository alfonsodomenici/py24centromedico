from flask import Blueprint

api = Blueprint('api',__name__,url_prefix='/api')

from .usersResource import users
api.register_blueprint(users)

from .checkpointsResource import checkpoints
api.register_blueprint(checkpoints)

from .reservationsResource import reservations
api.register_blueprint(reservations)