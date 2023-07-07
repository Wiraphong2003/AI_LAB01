# syntax=docker/dockerfile:1
FROM python:3.10.12-slim-bullseye
WORKDIR /AI-Class
EXPOSE 5000
ENV FLASK_APP=main.py
COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt
COPY . .
ENTRYPOINT [ "flask"]
CMD [ "run", "--host", "0.0.0.0" ]
