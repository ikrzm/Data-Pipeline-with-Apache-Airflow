import psycopg2 as db
from psycopg2 import Error, OperationalError
import os


from faker import Faker
import random
from time import sleep


def generate_data():
    fake = Faker()
    list_rows = []
    nb_row = random.randint(1000, 1200)
    for i in range(nb_row):
        list_rows.append(
            (i, fake.first_name(), fake.last_name(), fake.job(), fake.address(), fake.phone_number() )
        )
    return list_rows

def create_connexion(**kwargs):
    conn = None
    try:
        conn = db.connect(
            host=kwargs['pg_host'],
            port=kwargs['pg_port'],
            user=kwargs['pg_user'],
            password=kwargs['pg_password'],
            database=kwargs['pg_database']
        )
        print("Connection to PostgreSQL DB successful")
        return conn
    except OperationalError as e:
        print(f"Failed to connect to the database")
    return conn


def insert_data(**kwargs):
    sql = "INSERT INTO utilisateurs VALUES(%s, %s, %s, %s, %s, %s)"
    data = generate_data()
    conn = create_connexion(**kwargs)
    try:
        cur = conn.cursor()
        cur.executemany(sql, data)
        print('insertion successful')
        conn.commit()
        cur.close()
    except (Exception, db.DatabaseError)  as error:
        print(error)

def read_data(**kwargs) :

    conn = create_connexion(**kwargs)
    cur = conn.cursor()
    sql = "SELECT * FROM utilisateurs"
    cur.execute(sql)
    data = cur.fetchall()
 
    if not data:
        print("no data found")
        data = []
    conn.commit()
    return data

