ARG PYTHON_VERSION=3.6.8
FROM python:${PYTHON_VERSION}

WORKDIR /opt/server
COPY . .

RUN pip install -r requirements.txt

EXPOSE 5000
ENTRYPOINT ["/usr/local/bin/python3", "app.py"]