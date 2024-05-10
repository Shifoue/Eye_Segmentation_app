FROM nvidia/cuda:12.1.1-base-ubuntu22.04

WORKDIR /service/backend

RUN pip install -r requirements.txt

CMD ["python flask –app ressources/app.py run"]

EXPOSE 5000