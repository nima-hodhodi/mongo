FROM docker.arvancloud.ir/python:3.9-slim

WORKDIR /app

COPY app.py .

RUN pip install pymongo

CMD ["python","app.py"]
