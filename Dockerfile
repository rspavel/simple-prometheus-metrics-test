FROM  python:slim-bullseye

RUN pip install prometheus_client

ADD simple_metrics.py .

CMD ["python", "./simple_metrics.py"]
