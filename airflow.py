from airflow import DAG
from airflow.providers.databricks.operators.databricks import DatabricksRunNowOperator
from airflow.utils.dates import days_ago
from datetime import timedelta

default_args = {
    'owner': 'pradeep',
    'depends_on_past': False,
    'email': ['pradeepmummadireddy@gmail.com'],
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
}

with DAG(
    dag_id='databricks_single_job_orchestration',
    default_args=default_args,
    description='Orchestrates the multi-task Sales Pipeline in Databricks',
    schedule_interval='0 7 * * *',
    start_date=days_ago(1),
    tags=['sales', 'production', 'databricks'],
    catchup=False
) as dag:

    run_full_pipeline = DatabricksRunNowOperator(
        task_id='run_full_pipeline',
        databricks_conn_id='databricks_default',
        job_id=845047903077930
    )

    run_full_pipeline