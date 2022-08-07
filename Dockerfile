# FROM python:3.10-alpine
FROM ubuntu

WORKDIR app/

COPY requirements.txt .

RUN apt-get update
RUN apt-get install -y python3
RUN apt-get install -y python3-pip
RUN pip install -U pip
RUN pip install -r requirements.txt
RUN apt-get install -y openssh-server
RUN systemctl ssh start
RUN systemctl status ssh

COPY . .

ENTRYPOINT ["pytest"]
