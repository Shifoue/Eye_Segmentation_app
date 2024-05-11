FROM nvidia/cuda:12.1.1-base-ubuntu22.04

WORKDIR /services
COPY . .

RUN apt-get update
RUN apt-get install python3.10 -y
RUN apt install curl -y

RUN curl -o checkpoint_85_ADAMW.pth https://github.com/Shifoue/Eye_Segmentation_app/releases/download/Base_version/checkpoint_85_ADAMW.pth
COPY ../checkpoint_85_ADAMW.pth /services/backend/network/weights/

RUN apt install python3-pip -y
RUN pip install -U pip

RUN pip install -r requirements.txt

ENV FLASK_RUN_HOST=0.0.0.0
ENV FLASK_APP=app.py

CMD ["flask", "run", "--debug"]

EXPOSE 5000