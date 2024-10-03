FROM apache/airflow:2.9.2
RUN pip install -U pip
COPY requirements.txt /tmp/requirements.txt
RUN pip install --no-cache-dir -r /tmp/requirements.txt