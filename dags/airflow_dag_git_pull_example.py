from datetime import timedelta

import git
import airflow
from airflow import DAG
from airflow.operators.bash_operator import BashOperator


# These args will get passed on to each operator
# You can override them on a per-task basis during operator initialization
default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'start_date': airflow.utils.dates.days_ago(2),
    'email': ['airflow@example.com'],
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
    # 'queue': 'bash_queue',
    # 'pool': 'backfill',
    # 'priority_weight': 10,
    # 'end_date': datetime(2016, 1, 1),
    # 'wait_for_downstream': False,
    # 'dag': dag,
    # 'adhoc':False,
    # 'sla': timedelta(hours=2),
    # 'execution_timeout': timedelta(seconds=300),
    # 'on_failure_callback': some_function,
    # 'on_success_callback': some_other_function,
    # 'on_retry_callback': another_function,
    # 'trigger_rule': u'all_success'
}

dag = DAG(
    'dag_git_pull_example',
    default_args=default_args,
    description='A simple tutorial DAG',
    schedule_interval=timedelta(days=1),
)

t1 = BashOperator(
    task_id='print_path',
    bash_command='pwd',
    dag=dag,
)
#note- while running bash command keep space at the end of sh script name
t2 = BashOperator(
    task_id='test_git_pull_in_airflow',
    bash_command='sh /Users/bhim.sella/airflow/scripts/bash_git_cmd.sh ',
    dag=dag)

t3 = BashOperator(
    task_id='run_dbt',
    bash_command='sh /Users/bhim.sella/airflow/scripts/bash_dbt_cmd.sh ',
    dag=dag,
)


t1 >> t2
t2 >> t3
