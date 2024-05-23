from flask import Blueprint, request
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
    nome,cognome,email,pwd = request.json.values()
    q = "insert into tbclienti (nome,cognome,usrmail,pwd) values ('%s','%s','%s','%s')" \
         % (nome,cognome,email,pwd)
    conn = db.connection
    cursor = conn.cursor()
    cursor.execute(q)
    conn.commit()
    lastid = cursor.lastrowid
    return str(lastid)