# Airflow image
FROM apache/airflow:2.8.0

# Install dependencies
RUN pip install --upgrade pip
RUN pip install pymongo