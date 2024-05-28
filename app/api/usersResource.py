from flask import Blueprint, request,json, Response
from http import HTTPStatus

from app import db
from .usersService import findAllUsers,createUser,findUser
from .reservationsService import findUserReservations,createUserReservation

users = Blueprint('users',__name__,url_prefix='/users')

@users.get("/")
def all():
    result = findAllUsers()
    return Response(response=json.dumps(result), status=HTTPStatus.OK, content_type='application/json')
    
@users.post("/")
def registration():
    nome,cognome,email,pwd = request.json.values()
    result = createUser(nome,cognome,email,pwd)
    return Response(response=json.dumps(result), status=HTTPStatus.CREATED, content_type='application/json')

@users.get("/<int:id>")
def find(id):
    user = findUser(id)
    return Response(response=json.dumps(user), status=HTTPStatus.OK, content_type='application/json')

@users.get("/<int:id>/reservations")
def findReservations(id):
    result = findUserReservations(id)
    return Response(response=json.dumps(result), status=HTTPStatus.OK, content_type='application/json')

@users.post("/<int:id>/reservations")
def createReservation(id):
    idvisita,data,pagato = request.json.values()
    result = createUserReservation(id,idvisita,data,pagato)
    return Response(response=json.dumps(result), status=HTTPStatus.CREATED, content_type='application/json')