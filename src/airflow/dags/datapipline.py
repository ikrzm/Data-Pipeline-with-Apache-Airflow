
import sys
sys.path.insert(0, '/opt/airflow/db_psql')
sys.path.insert(0, '/opt/airflow/db_mongo')
import datetime as dt
from airflow import DAG
from airflow.operators.python import PythonOperator
from airflow.operators.bash import BashOperator
from db_man import insert_data
from mgdb_man import insert_data_mongo
default_args = {
        'owner' : 'airflow',
        'start_date' : dt.datetime(2022, 11, 12)
}


with DAG(
    dag_id="ingest_data_postgres",
    default_args=default_args,
    schedule_interval='@once'
) as dag:
    task_1 = BashOperator(
    task_id ="bash_echo",
    bash_command='echo "starting ingestinf fake data to postgres"'
    )
    task_2 = PythonOperator(
    task_id ="postgres_ingestion",
    python_callable=insert_data,
    op_kwargs= {
        'pg_host' : 'postgres',
        'pg_port': '5432',
        'pg_user': 'postgres',
        'pg_password': 'postgres',
        'pg_database' : 'users'
    }
    )
    task_3 = PythonOperator(
        task_id = 'mongo_ingestion',
        python_callable=insert_data_mongo,
        op_kwargs= {
            'pg_host' : 'postgres',
            'pg_port': '5432',
            'pg_user': 'postgres',
            'pg_password': 'postgres',
            'pg_database' : 'users',
            'mg_user' : 'root',
            'mg_pass' : 'root',
            'mg_port' : '27017',
            'mg_host' : 'mongo'
        }
    )
    task_1 >> task_2 >> task_3