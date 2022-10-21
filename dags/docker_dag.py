from airflow.decorators import task, dag
from airflow.providers.docker.operators.docker import DockerOperator

from datetime import datetime

@dag(start_date=datetime(2022,1,1), schedule_interval='@daily', catchup=False)


def docker_dag():

    @task()
    def t1():
        pass

    t2 = DockerOperator(
        task_id='t2',
        api_version='auto',
        container_name='task_t2',
        image='python:3.8-slim-buster',
        command='bash /tmp/scripts/output.sh"',
        docker_url='unix://var/run/docker.sock',
        network_mode='bridge',
        xcom_all=True,
        retrieve_output=True,
        retrieve_output_path='/tmp/script.out',
        auto_remove=True,
        mount_tmp_dir=False,
        mounts=[
            Mount(source='/Users/Gabriel/Documents/materials/venv/scripts', target='/tmp/scripts', type='bind')
        ]
    )

    t1() >> t2

docker = docker_dag()