FROM nvidia/cuda:12.1.1-base-ubuntu22.04

COPY . .
WORKDIR /services

RUN apt-get update

# Debug
RUN apt install curl -y
RUN apt install vim -y

# Needed
RUN apt install wget -y
RUN wget https://github.com/Shifoue/Eye_Segmentation_app/releases/download/Base_version/checkpoint_85_ADAMW.pth

RUN mkdir /services/backend/network/weights
RUN mv checkpoint_85_ADAMW.pth /services/backend/network/weights/

RUN apt-get install python3.10 -y
RUN apt install python3-pip -y
RUN pip install -U pip
RUN apt install zlib1g-dev libjpeg-dev libpng-dev -y

RUN pip install -r requirements.txt

EXPOSE 5000

CMD ["flask", "run", "--host=0.0.0.0", "--cert=adhoc"]