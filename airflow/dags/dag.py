from airflow.operators.python_operator import PythonOperator
from airflow.operators.bash_operator import BashOperator
from airflow.utils.task_group import TaskGroup
from airflow.models import Variable
from airflow.operators.docker_operator import DockerOperator


from datetime import datetime, timedelta
from airflow import DAG
import sys

sys.path.append('/opt/Scripts/')
from extract import extract
from insert_json_into_mongodb import insert_json_into_mongodb
from transform import transform
from create_postgres_tables import create_postgres_tables
from load import load
from check_postgre_results import check_postgre_results
from check_mongodb_results import check_mongodb_results
from create_postgres_database import create_postgres_database

default_args={
    'owner': 'Fran',
    'retries':5,
    'retry_delay': timedelta(minutes=5)
}

with DAG(
    default_args=default_args,
    dag_id='Pokemon_api_extract',
    description= 'Extract Json from pokemon_api.',
    start_date=datetime(2024,1,21)
    ) as dag:

    task1 = PythonOperator(
        task_id='Pokemon_api_extract',
        python_callable=extract,
        dag=dag
    )

    task2 = PythonOperator(
        task_id='create_mongodb_db_and_collection',
        python_callable= insert_json_into_mongodb,
    )

    task3 = PythonOperator(
        task_id='transform',
        python_callable= transform,
    )

    task4a = PythonOperator(
        task_id='create_postgres_database',
        python_callable= create_postgres_database,
    )

    task4b = PythonOperator(
        task_id='create_postgres_tables',
        python_callable= create_postgres_tables,
    )

    task5 = PythonOperator(
        task_id='load',
        python_callable= load,
    )

    task6 = PythonOperator(
        task_id='check_postgre_results',
        python_callable= check_postgre_results,
    )

    task7 = PythonOperator(
        task_id='check_mongodb_results',
        python_callable= check_mongodb_results,
    )

task1 >> task2 >> task3
task4a >> task4b
task3 >> task5
task4b >> task5
task5 >> task6
task5 >> task7