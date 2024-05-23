from flask import Blueprint,request
from .checkupsService import findAllCheckups, createCheckup

checkups=Blueprint('checkups',__name__,url_prefix='/checkups')

@checkups.get('/')
def all():
    result = findAllCheckups()
    return str(result)

@checkups.post("/")
def create():
    tipo,costo=request.json.values()
    result = createCheckup(tipo,costo)
    return str(result)