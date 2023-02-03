FROM python:3-alpine

WORKDIR /app

COPY ./requirements.txt requirements.txt
RUN pip install -r requirements.txt

COPY . .

ENV PORT=8000
EXPOSE $PORT
ENTRYPOINT python server.py
