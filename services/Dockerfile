FROM nvidia/cuda:12.1.1-base-ubuntu22.04

WORKDIR /services
COPY /services/ .

RUN apt-get update
RUN apt-get install python3.10 -y

RUN apt install python3-pip -y
RUN pip install -U pip

RUN pip install -r requirements.txt

ENV FLASK_RUN_HOST=0.0.0.0
ENV FLASK_APP=app.py

CMD ["flask", "run", "--debug"]

EXPOSE 5000