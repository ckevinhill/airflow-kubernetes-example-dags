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
    'kubernetes_operator_example', default_args=default_args, schedule_interval=timedelta(minutes=10))


task = KubernetesPodOperator(namespace='airflow',
                            image="Python:3.6",
                            cmds=["Python","-c"],
                            arguments=["print('hello world')"],
                            labels={"foo": "bar"},
                            in_cluster=True,
                            name="python-task",
                            task_id="python-task",
                            get_logs=True,
                            dag=dag
                          )


