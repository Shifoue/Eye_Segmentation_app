FROM nvidia/cuda:12.1.1-base-ubuntu22.04

WORKDIR /service/backend

RUN pip install -r requirements.txt

ENV FLASK_RUN_HOST=0.0.0.0
ENV FLASK_APP=ressources/app.py

CMD ["flask", "run", "--debug"]

EXPOSE 5000