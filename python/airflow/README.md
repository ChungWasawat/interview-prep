# Airflow
main components
- web server
    - Airflow’s user interface (UI), available at `localhost:8080`
- executor
    - choose one that is suitable for each job like `CeleryExecutor` for better scalability or `KubernetesExecutor` for kubernetes features 
- scheduler
    - is resposible to execute different tasks at the correct time: monitoring all tasks, backfilling data, ensuring task completion
- postgresql (above 12)
    - contain all pipelines metadata
    - other sql databases are also supported
## Installation
[start commands](https://airflow.apache.org/docs/apache-airflow/stable/start.html)
[more details of each installation method](https://airflow.apache.org/docs/apache-airflow/stable/installation/index.html#using-managed-airflow-services)
### Executor
- CeleryExecutor
    - need extra postgresql for backend
    - need redis for broker 
    - need to set airflow worker (celery worker)
    - need to set flower (celery flower) to monitor environment, available at `localhost:5555`

### brief installation notes for me
#### on a machine
##### LocalExecutor
- create a virtual environment or use a default environment on a machine to install airflow
- `export AIRFLOW_HOME=.` set airflow home directory to current directory (to manage everything in a single directory)
- `airflow db init` start using airflow. This will create logs folder, configuration file, database file, etc.
- `airflow webserver -p 8080` start airflow webserver with the specific port (default=8080)
- `airflow users create --help` to show details how to create a user
    - example below
    - `airflow users create --username admin --firstname firstname --lastname lastname --role Admin --email admin@domain.com` press `enter` and then set password 
- `airflow scheduler` to start scheduler

#### on docker
- [the image on docker hub](https://hub.docker.com/r/puckel/docker-airflow)
- [step by step installation with docker](https://airflow.apache.org/docs/apache-airflow/stable/howto/docker-compose/index.html)
- need memory at least 5GB (8GB ideally)
##### CeleryExecutor
- download yaml file `curl -LfO 'https://airflow.apache.org/docs/apache-airflow/2.10.2/docker-compose.yaml'`
- customize its content before start running
- create these folders `mkdir -p ./dags ./logs ./plugins ./config`
    - mounted folders between local machine and container
        - `dags` for DAG files storage
        - `logs` to contains logs from task execution scheduler
        - `plugins` for custom plugins
- set airflow uid and gid in `.env`
```
echo -e "AIRFLOW_UID=$(id -u)" > .env
echo -e "AIRFLOW_GID=$(id -g)" > .env
```
- initialize airflow with `docker-compose up airflow-init`
- after installation complete, 
    - `docker-compose up` to run airflow
        - `-d` to run airflow in detached mode
        - `--no-deps` to start the specified service(s) without starting any linked or dependent services
        - `--build <service-name> (<service-name> ..)` to build images before run container 
- to turn off the service
    - `docker-compose down` to turn off all services
        - `--volumes` to turn off, remove volumes (or use `-v`) 
        - `--remove-orphans` to remove any containers which started by docker compose
        - `--rmi` to remove all images associated with the services
- delete the folder with `rm -rf '<DIRECTORY>'` 
- add external packages to the container
    - image extending 
        - choose one of these
            - create a dockerfile and put all needed packages there and build the image with `docker build -t apache/airflow:2.1.0 .` 
                - it should be the same like in the image in docker-compose.yml `${AIRFLOW_IMAGE_NAME:-apache/airflow:2.1.0}`
            - build the image with `docker-compose build` 
                - just set value in these parts 
                    - "build: " 
                    - "image: "
    - image customizing 
        - clone [this repository](https://github.com/apache/airflow)
        - add `requirements.txt` at `docker-context-files` directory
        - build an image from that
        - edit the image name to the new one
- to use airflow command to container 
```
docker ps                               # to find a container of airflow scheduler
docker exec -it <container_id> bash     # to log in to container, and then use airflow command 
```
##### LocalExecutor
- overall, it's like `CeleryExecutor` but remove something.
- remove `AIRFLOW__CELERY__RESULT_BACKEND` and `AIRFLOW__CELERY__BROKER_URL` from `environment` part
- remove `redis`, `airflow-worker`, `airflow-triggerer` and `flower` from services

###### to connect to google cloud
+ create a directory at home to store a key and be mapped from container 
```
    cd ~ && mkdir -p ~/.google/credentials/
    mv <path/to/your/service-account-authkeys>.json ~/.google/credentials/google_credentials.json
```
+ remove the image tag, to replace it with your build from your Dockerfile, as shown
+ add `GOOGLE_APPLICATION_CREDENTIALS`, `AIRFLOW_CONN_GOOGLE_CLOUD_DEFAULT`, `GCP_PROJECT_ID`, `GCP_GCS_BUCKET` to allow airflow to connect to gcp
+ if docker-compose can't find the folder, can add the part below in `docker-compose.yml` 
```
  volumes:
    - ./dags:/opt/airflow/dags
    - ./logs:/opt/airflow/logs
    - ./plugins:/opt/airflow/plugins
    # here: ----------------------------
    - c:/Users/alexe/.google/credentials/:/.google/credentials:ro
    # -----------------------------------
```

## Commands
- `airflow dags list` to list all dags
- `airflow dags backfill -s 2024-09-25 -e 2024-09-28 <dag_id>` to execute backfilling
- `airflow tasks list <dag_id>` to list all tasks in the dag
    - `--tree` to show in hierarchy
- `airflow test <dag_id> <task_id> 2024-09-28` to test a task in specific dag
    - `airflow tasks test <dag_id> <task_id> 2024-09-28` 

## Connections
#### postgresql
- for postgresql of a docker container
    - conn id: anything, postgresql_localhost in this case
    - conn type: postgres
    - host: host.docker.internal
    - schema: anything, test
    - login: airflow
    - port: 5432 

## Emails 
### local
- can see from `airflow.cfg` in email part
### docker
#### add varables in `docker-compose.yml`
- add these variables at the top of `docker-compose.yml` (config part)
- for gmail, need to enable 2step authentication and set app password before using
```
x-airflow-common:
    environment:
        AIRFLOW__EMAIL__EMAIL_BACKEND: airflow.utils.email.send_email_smtp
        AIRFLOW__SMTP__SMTP_HOST: smtp.gmail.com / smtp.outlook365.com
        AIRFLOW__SMTP__SMTP_STARTTLS: True
        AIRFLOW__SMTP__SMTP_SSL: False
        AIRFLOW__SMTP__SMTP_USER: <your-email@gmail.com> / <your-email@outlook.com>
        AIRFLOW__SMTP__SMTP_PASSWORD_FILE: /run/secrets/smtp_password
        AIRFLOW__SMTP__SMTP_PORT: 587
        AIRFLOW__SMTP__SMTP_MAIL_FROM: <your-from-email>
    secrets:
        - smtp_password
secrets:
  smtp_password:
    file: ./smtp_password.txt
```
#### add through connections
- conn_id: smtp_default, or anything
- conn_type: email
- login: email-user
- passowrd: email-password

## Tips
- check python environment cafefully if airflow installed locally
- `python dags/dags_1.py` can help to check error
- if dag file doesn't show up, can reduce `dag_dir_list_interval` in `airflow.cfg`. then restart airflow
    - add `AIRFLOW__SCHEDULER__DAG_DIR_LIST_INTERVAL` in docker-compose.yml if installed on docker
- `docker compose start airflow-scheduler` to run the container separately when scheduler does not running