FROM python:3.9.19-slim-buster

RUN apt update -y && apt install awscli -y
WORKDIR /main

COPY . /main/
RUN pip install -r requirements.txt

CMD ["python3", "main.py"]
