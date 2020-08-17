From python:3.6.10-slim-stretch
WORKDIR /usr/src/app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt && apt-get update && apt-get install -y wget curl

COPY . .

EXPOSE 5000

CMD [ "python", "./Api.py"]

