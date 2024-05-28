from flask import Blueprint,Response,json
from http import HTTPStatus
from .reservationsService import findAllReservations

reservations=Blueprint('reservations',__name__,url_prefix='/reservations')

@reservations.get('/')
def all():
    result=findAllReservations()
    return Response(response=json.dumps(result), status=HTTPStatus.OK, content_type='application/json')