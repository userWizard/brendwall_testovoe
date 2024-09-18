FROM python:3.12.1-slim-bullseye

RUN mkdir /app

COPY requirements.txt /app

RUN pip3 install -r /app/requirements.txt --no-cache-dir

COPY . /app

WORKDIR /app

CMD ["python3", "manage.py", "runserver", "0:8000"] 