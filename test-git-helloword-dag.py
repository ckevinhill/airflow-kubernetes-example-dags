from datetime import datetime
from airflow import DAG
from airflow.operators.dummy_operator import PythonOperator

dag = DAG('hello_world_via_git', description='Git sync test', schedule_interval='0 12 * * *', start_date=datetime(2017, 3, 20), catchup=False)

def print_hello():
    print ("hello")

def print_there():
    print("there")

def print_world():
    print("world")

hello_operator = PythonOperator(
    task_id='hello_task',
    python_callable=print_hello,
    dag=dag,
)

there_operator = PythonOperator(
    task_id='there_task',
    python_callable=print_there,
    dag=dag,
)

world_operator = PythonOperator(
    task_id='world_task',
    python_callable=print_world,
    dag=dag,
)


hello_operator >> there_operator >> world_operator