FROM python:3.7
WORKDIR /app
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt
EXPOSE 8080
CMD gunicorn --workers=1 --bind 0.0.0.0:8080 app:app
COPY . /app