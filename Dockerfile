FROM apache/airflow:latest
WORKDIR /project-root
COPY . .
ADD requirements.txt .
RUN pip install -r requirements.txt