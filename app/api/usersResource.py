from flask import Blueprint
from app import db

users = Blueprint('users',__name__,url_prefix='/users')

@users.get("/")
def all():
    cur = db.connection.cursor()
    cur.execute("""SELECT nome,cognome,usrmail FROM tbclienti""")
    rv = cur.fetchall()
    return str(rv)
    
@users.post("/")
def registration():
    return 'registration ok'