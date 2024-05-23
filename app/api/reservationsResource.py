from flask import Blueprint
from .reservationsService import findAllReservations

reservations=Blueprint('reservations',__name__,url_prefix='/reservations')

@reservations.get('/')
def all():
    result=findAllReservations()
    return str(result)