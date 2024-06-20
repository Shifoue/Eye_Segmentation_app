FROM nginx:latest

WORKDIR /services/etc/nginx

RUN apt-get update
# Debug
RUN apt install curl -y
RUN apt install vim -y

#Needed
RUN apt-get install python3.10 -y
RUN apt install python3-pip -y
# RUN pip install -U pip

RUN apt install python3-pyOpenSSL

# RUN pip install pyOpenSSL

# Remove any existing config files
#RUN rm /etc/nginx/conf.d/*
RUN rm nginx.conf

RUN openssl req -x509 -nodes -days 365 -newkey rsa:2048 -keyout /etc/ssl/private/selfsigned.key -out /etc/ssl/certs/selfsigned.crt
#RUN rm -f /etc/nginx/sites-enabled/default
# Copy the custom Nginx configuration
COPY /services/etc/nginx/nginx.conf .

COPY /services/etc/nginx/sites-available/reverse-proxy.conf /sites-available/reverse-proxy.conf

# # Expose port 80 for Nginx

RUN ln -s /services/etc/nginx/sites-available/reverse-proxy.conf /sites-enabled/

EXPOSE 80