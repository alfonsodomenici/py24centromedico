from flask import Blueprint

reservations=Blueprint('reservations',__name__,url_prefix='/reservations')

@reservations.get('/')
def all():
    return 'all reservations'