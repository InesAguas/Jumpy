import psycopg2

#base de dados
def initConnection():
    host = "ec2-52-31-201-170.eu-west-1.compute.amazonaws.com"
    database = "d3oqchd1gmho16"
    user = "xccnazbfpqayyb"
    password = "af63e93d8435072bcd7640a39cba9dd1737d4811fe3f63854d4ffc673b5d345f"
    conn = psycopg2.connect(host=host, dbname=database, user=user, password=password)
    cur = conn.cursor()
    return conn, cur

def inserirDados(username, coins, time):
    #connect to database
    conn, cur = initConnection()
    #insert command
    query = """INSERT INTO public."scores"(
    username, coins, time)
    VALUES (%s, %s, %s);"""
    cur.execute(query, [username, coins, time])
    conn.commit()
    conn.close()

def mostrarDados():
    #connect to database
    conn, cur = initConnection()

    cur.execute("""SELECT * 
    FROM public."scores"
    ORDER BY coins DESC, time ASC, username
    LIMIT 10;""")
    resultados = cur.fetchall()
    conn.close()
    return resultados   


