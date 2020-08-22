from airflow import DAG
from datetime import datetime, timedelta
from airflow.contrib.operators.kubernetes_pod_operator import KubernetesPodOperator
from airflow.operators.dummy_operator import DummyOperator


default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'start_date': datetime.utcnow(),
    'email': ['airflow@example.com'],
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 1,
    'retry_delay': timedelta(minutes=5)
}

dag = DAG(
        'test_kubernetes_operator', 
        default_args=default_args, 
        schedule_interval='@daily' ) 


hello_task = KubernetesPodOperator(namespace='airflow',
                            image="python:3.8-slim-buster",
                            cmds=["python","-c"],
                            arguments=["print('hello')"],
                            labels={"foo": "bar"},
                            in_cluster=True,
                            name="hello_task",
                            task_id="hello_task",
                            get_logs=True,
                            is_delete_operator_pod=True,
                            dag=dag
                          )

world_task = KubernetesPodOperator(namespace='airflow',
                            image="python:3.8-slim-buster",
                            cmds=["python","-c"],
                            arguments=["print('world')"],
                            labels={"foo": "bar"},
                            in_cluster=True,
                            name="world_task",
                            task_id="world_task",
                            get_logs=True,
                            is_delete_operator_pod=True,
                            dag=dag
                          )

hello_task >> world_task