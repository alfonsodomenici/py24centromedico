from flask import Blueprint, request,json
from app import db
from .usersService import findAllUsers,createUser,findUser
from .reservationsService import findUserReservations,createUserReservation

users = Blueprint('users',__name__,url_prefix='/users')

@users.get("/")
def all():
    result = findAllUsers()
    return str(result)
    
@users.post("/")
def registration():
    nome,cognome,email,pwd = request.json.values()
    id = createUser(nome,cognome,email,pwd)
    return str(id)

@users.get("/<int:id>")
def find(id):
    user = findUser(id)
    return str(user)

@users.get("/<int:id>/reservations")
def findReservations(id):
    result = findUserReservations(id)
    return str(result)

@users.post("/<int:id>/reservations")
def createReservation(id):
    idvisita,data,pagato = request.json.values()
    result = createUserReservation(id,idvisita,data,pagato)
    return str(result)