from app import db

def findAllCheckups():
    cur = db.connection.cursor()
    cur.execute("SELECT * FROM tbvisite")
    return  cur.fetchall()

def findCheckupById(id):
    cur = db.connection.cursor()
    cur.execute(f"SELECT * FROM tbvisite where idvisita={id}")
    return  cur.fetchone()    

def createCheckup(tipo,costo):
    conn = db.connection
    cur = conn.cursor()
    cur.execute(f"insert into tbvisite (tipo,costo) values('{tipo}',{costo})")
    conn.commit()
    lastId=cur.lastrowid
    return  lastId