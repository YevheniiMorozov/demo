FROM python:3.10

WORKDIR usr/src/app

COPY requirements.txt ./

RUN pip install -r requirements.txt && rm -rf /root/.cache/pip

COPY . .

EXPOSE 5000

