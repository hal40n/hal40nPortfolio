FROM python:3.12-slim

WORKDIR /app

COPY ./requirements.txt /app/

COPY .env /app/

RUN pip install --no-cache-dir -r requirements.txt

COPY . /app

EXPOSE 8001
EXPOSE 8002

CMD ["sh", "/app/run_apps.sh"]
