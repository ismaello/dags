from airflow.contrib.operators.kubernetes_pod_operator import KubernetesPodOperator
from airflow.kubernetes.secret import Secret
from airflow.models import DAG
from airflow.utils.dates import days_ago


default_args = {
    'owner': 'Airflow',
    'start_date': days_ago(2)
}

dag=DAG(
    dag_id='test_isc_k8s',
    default_args=default_args,
    schedule_interval=None
) 
k = KubernetesPodOperator(
    namespace='airflow',
    image="ubuntu:16.04",
    cmds=["bash", "-cx"],
    arguments=["echo", "10"],
    name="airflow-test-pod",
    task_id="task",
    get_logs=True,
    is_delete_operator_pod=True,
    dag=dag
)
