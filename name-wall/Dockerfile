FROM python:alpine3.14

WORKDIR /name-wall
COPY . .

RUN pip install --upgrade pip
RUN pip install psycopg2-binary
RUN pip install -r requirements.txt

CMD ["python3", "./app.py"]
