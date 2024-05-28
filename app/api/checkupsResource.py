from flask import Blueprint,request,Response,json
from http import HTTPStatus
from .checkupsService import findAllCheckups, createCheckup

checkups=Blueprint('checkups',__name__,url_prefix='/checkups')

@checkups.get('/')
def all():
    result = findAllCheckups()
    return Response(response=json.dumps(result), status=HTTPStatus.OK, content_type='application/json')

@checkups.post("/")
def create():
    tipo,costo=request.json.values()
    id = createCheckup(tipo,costo)
    result={
        'id':id
    }
    return Response(response=json.dumps(result), status=HTTPStatus.CREATED, content_type='application/json')