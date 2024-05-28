from flask import Blueprint,request,json,Response
from http import HTTPStatus
from passlib.hash import pbkdf2_sha256
from .usersService import findUserByEmail
from flask_jwt_extended import create_access_token, jwt_required
auths = Blueprint('auths',__name__, url_prefix='/auths')

@auths.post("/")
def login():
    email,pwd = request.json.values()
    found = findUserByEmail(email)
    if found is None:
        return Response(response="login failed", status=HTTPStatus.FORBIDDEN, content_type='text/plain')
    
    pwdCheck = pbkdf2_sha256.verify(pwd,found['pwd'])
    if not pwdCheck:
        return Response(response="login failed", status=HTTPStatus.FORBIDDEN, content_type='text/plain')
    claims={
        'name':found['usrmail']
    }
    accessToken = create_access_token(identity=found['idcliente'], 
        additional_claims=claims)
    result = {
        "token":accessToken
    }
    return Response(response=json.dumps(result), status=HTTPStatus.OK, content_type='application/json')