from flask import Blueprint, request,json, Response
from http import HTTPStatus
from passlib.hash import pbkdf2_sha256  
from app import db
from flask_jwt_extended import jwt_required, get_jwt_identity, verify_jwt_in_request
from .usersService import findAllUsers,createUser,findUser
from .reservationsService import findUserReservations,createUserReservation

users = Blueprint('users',__name__,url_prefix='/users')

@users.get("/")
@jwt_required()
def all():
    result = findAllUsers()
    return Response(response=json.dumps(result), status=HTTPStatus.OK, content_type='application/json')
    
@users.post("/")
def registration():
    nome,cognome,email,pwd = request.json.values()
    hash=pbkdf2_sha256.hash(pwd)
    result = createUser(nome,cognome,email,hash)
    return Response(response=json.dumps(result), status=HTTPStatus.CREATED, content_type='application/json')

@users.get("/<int:id>")
@jwt_required()
def find(id):
    sub = get_jwt_identity()
    if id != sub:
        return Response(response="access is not allowed", status=HTTPStatus.FORBIDDEN, content_type='text/plain')
    
    user = findUser(id)
    return Response(response=json.dumps(user), status=HTTPStatus.OK, content_type='application/json')

@users.get("/<int:id>/reservations/")
@jwt_required()
def findReservations(id):
    sub = get_jwt_identity()
    if id != sub:
        return Response(response="access is not allowed", status=HTTPStatus.FORBIDDEN, content_type='text/plain')
    
    result = findUserReservations(id)
    return Response(response=json.dumps(result), status=HTTPStatus.OK, content_type='application/json')

@users.post("/<int:id>/reservations/")
@jwt_required()
def createReservation(id):
    sub = get_jwt_identity()
    if id != sub:
        return Response(response="access is not allowed", status=HTTPStatus.FORBIDDEN, content_type='text/plain')
    
    idvisita,data,pagato = request.json.values()
    result = createUserReservation(id,idvisita,data,pagato)
    return Response(response=json.dumps(result), status=HTTPStatus.CREATED, content_type='application/json')