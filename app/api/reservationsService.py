from app import db

def findAllReservations():
    cursor = db.connection.cursor()
    q = f"""
        select p.idprenotazioni,p.data,c.nome,c.cognome,v.tipo,v.costo,p.pagato from tbprenotazioni p 
        join tbvisite v on p.idvisita=v.idvisita
        join tbclienti c on p.idcliente=c.idcliente
        order by data asc
        """
    cursor.execute(q)
    return cursor.fetchall()

def findUserReservations(userId):
    cursor = db.connection.cursor()
    q = f"""
        select p.idprenotazioni,p.data,v.tipo,v.costo,p.pagato from tbprenotazioni p 
        join tbvisite v on p.idvisita=v.idvisita
        where p.idcliente={userId}
        order by data asc
        """
    cursor.execute(q)
    return cursor.fetchall()

def createUserReservation(idcliente,idvisita,data,pagato):

    q = f"""
        insert into tbprenotazioni (idcliente,idvisita,data,pagato) 
        values ({idcliente},{idvisita},'{data}',{pagato}) 
        """
    print(q)
    conn = db.connection
    cursor = conn.cursor()
    cursor.execute(q)
    conn.commit()
    lastid = cursor.lastrowid
    return lastid