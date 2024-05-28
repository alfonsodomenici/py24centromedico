from app import db

def findAllUsers():
    cur = db.connection.cursor()
    cur.execute("SELECT nome,cognome,usrmail FROM tbclienti")
    return  cur.fetchall()

def createUser(nome,cognome,email,pwd):
    q = f"""
        insert into tbclienti (nome,cognome,usrmail,pwd) 
        values ('{nome}','{cognome}','{email}','{pwd}')
        """
    conn = db.connection
    cursor = conn.cursor()
    cursor.execute(q)
    conn.commit()
    lastid = cursor.lastrowid
    return findUser(lastid)

def findUser(id):
    cursor = db.connection.cursor()
    q = f"""select idcliente,nome,cognome,usrmail 
        from tbclienti 
        where idcliente={id}
        """
    cursor.execute(q)
    return cursor.fetchone()

