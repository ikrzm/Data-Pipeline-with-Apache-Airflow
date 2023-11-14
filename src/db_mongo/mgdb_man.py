
import pymongo as mdb
import sys
import os
from pymongo.errors import ConnectionFailure, ConfigurationError, PyMongoError

import sys
sys.path.insert(0, '/opt/airflow/db_psql')
from db_man import read_data



# MongoDB connection 

def mgdb_create_connexion(**kwargs) :
    mongo_user = kwargs['mg_user']
    mongo_password = kwargs['mg_pass']
    mongo_port = kwargs['mg_port']
    mongo_host = kwargs['mg_host']
    mg_client=None
    try:
        mg_client = mdb.MongoClient(
            f"mongodb://{mongo_user}:{mongo_password}@{mongo_host}:{mongo_port}/"
        )
        mg_client.admin.command('ping')
        print('---------- connexion succefull ---------------')
        return mg_client
    except ConnectionFailure:
        print("Failed to connect to MongoDB, check your connection settings.")
    except ConfigurationError:
        print("There was a configuration error in the MongoDB connection.")
    except PyMongoError as e:
        print(f"An error occurred with MongoDB: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

    return None


def insert_data_mongo(**kwargs) :

    mg_conn = mgdb_create_connexion(**kwargs)
    
    pg_data = read_data(**kwargs)
    db = mg_conn['users']
    collection = db['users']
    for row in pg_data:
        document = {
        'id': row[0],
        'first_name': row[1],
        'last_name': row[2],
        'job': row[3],
        'address': row[4],
        'phone_number': row[5]
        }
        collection.insert_one(document)
    print('------- insertion succefull ------')