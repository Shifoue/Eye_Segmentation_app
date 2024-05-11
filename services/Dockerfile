FROM nvidia/cuda:12.1.1-base-ubuntu22.04

WORKDIR /services

RUN apt-get update
RUN apt-get install python3.10 -y

RUN python -m ensurepip --upgrade -y

RUN pip install -r requirements.txt

ENV FLASK_RUN_HOST=0.0.0.0
ENV FLASK_APP=app.py

CMD ["flask", "run", "--debug"]

EXPOSE 5000