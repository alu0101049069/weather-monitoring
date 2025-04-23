FROM python:3.10

WORKDIR /app

COPY temperature_exporter.py . 

RUN pip install requests prometheus_client

CMD ["python", "temperature_exporter.py"]
