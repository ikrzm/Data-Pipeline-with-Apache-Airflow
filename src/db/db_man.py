import psycopg2 as db
from psycopg2 import Error, OperationalError
import os
from fake_data import generate_data

def create_connexion() :
    conn = None
    print(os.getenv('POSTGRES_USER'))
    print(os.getenv('POSTGRES_PASSWORD'))
    try:
        conn = db.connect(host = "db",
                        port = "5432",
                        user = os.getenv('POSTGRES_USER'),
                        password = os.getenv('POSTGRES_PASSWORD'),
                        database = os.getenv('POSTGRES_DB')
                        )
        print("Connexion to Postgresql db successful")
    except OperationalError as e:
        print(f"The error '{e}' occured")
    return conn

def insert_data(conn):
    sql = "INSERT INTO utilisateurs VALUES(%s, %s, %s, %s, %s, %s)"
    data = generate_data()
    try:
        cur = conn.cursor()
        cur.executemany(sql, data)
        conn.commit()
        cur.close()
    except (Exception, db.DatabaseError)  as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()
