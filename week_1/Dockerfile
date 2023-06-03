FROM python:3.8-slim-buster

RUN pip install pandas psycopg2-binary sqlalchemy
RUN apt-get update \
    && apt-get install wget -y --no-install-recommends \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /pipelines
COPY ingest_taxi_data.py .

ENTRYPOINT ["python", "ingest_taxi_data.py"]
