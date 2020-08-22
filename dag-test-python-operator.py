from datetime import datetime
from airflow import DAG
from airflow.operators.python_operator import PythonOperator

dag = DAG(
        'test_python_operator', 
        description='DAG to test PythonOperator', 
        schedule_interval='@daily', 
        start_date=datetime(2020, 1, 1), 
        catchup=False )

def print_hello():
    print ("hello")

def print_world():
    print("world")

hello_task = PythonOperator(
    task_id='hello_task',
    python_callable=print_hello,
    dag=dag,
)

world_task = PythonOperator(
    task_id='world_task',
    python_callable=print_world,
    dag=dag,
)

hello_task >> world_task