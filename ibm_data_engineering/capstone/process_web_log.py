from datetime import timedelta
# The DAG object; we'll need this to instantiate a DAG
from airflow import DAG
# Operators; we need this to write tasks!
from airflow.operators.bash_operator import BashOperator
# This makes scheduling easy
from airflow.utils.dates import days_ago

# Defining DAG arguments

default_args = {
    'owner': 'Ocean Fish',
    'start_date': days_ago(0),
    'email': ['fishdummy@example.com'],
    'email_on_failure': True,
    'email_on_retry': True,
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
}

# Define the DAG

dag = DAG(
    'process_web_log',
    default_args=default_args,
    description='IBM Data Engineering Capstone',
    schedule_interval=timedelta(days=1),
)

# Define the tasks

extract_data = BashOperator(
    task_id='extract_data',
    bash_command='cut -d " " -f1 /home/project/airflow/dags/capstone/accesslog.txt > /home/project/airflow/dags/capstone/extracted_data.txt',
    dag=dag
)

transform_data = BashOperator(
    task_id='transform_data',
    bash_command='cat /home/project/airflow/dags/capstone/extracted_data.txt | grep "198.46.149.143" > /home/project/airflow/dags/capstone/transformed_data.txt',
    dag=dag
)

load_data = BashOperator(
    task_id='load_data',
    bash_command='tar -cvf /home/project/airflow/dags/capstone/weblog.tar /home/project/airflow/dags/capstone/transformed_data.txt',
    dag=dag
)

# task pipeline
extract_data >> transform_data >> load_data
