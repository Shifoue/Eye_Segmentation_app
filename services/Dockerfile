FROM nvidia/cuda:12.1.1-base-ubuntu22.04

WORKDIR /services

RUN apt-get update
RUN apt-get install python3.10 -y
RUN apt install curl -y

RUN curl -O https://github.com/Shifoue/Eye_Segmentation_app/releases/download/Base_version/checkpoint_85_ADAMW.pth
RUN cp checkpoint_85_ADAMW.pth /backend/network/weights/

RUN apt install python3-pip -y
RUN pip install -U pip

COPY . .

RUN pip install -r requirements.txt

ENV FLASK_RUN_HOST=0.0.0.0
ENV FLASK_APP=app.py

CMD ["flask", "run", "--debug"]

EXPOSE 5000