FROM nvidia/cuda:12.1.1-base-ubuntu22.04

WORKDIR /services

RUN sudo apt-get update
RUN sudo apt-get install python3.10

RUN python -m ensurepip --upgrade

RUN pip install -r requirements.txt

ENV FLASK_RUN_HOST=0.0.0.0
ENV FLASK_APP=app.py

CMD ["flask", "run", "--debug"]

EXPOSE 5000