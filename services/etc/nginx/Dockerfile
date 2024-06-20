FROM nginx:latest
# FROM ubuntu:22.04

# WORKDIR /etc/nginx

RUN apt-get update
# Debug
RUN apt install curl -y
RUN apt install vim -y
RUN apt install systemd -y

#Needed
# RUN apt install nginx -y
# RUN apt install ufw -y


# RUN ufw allow 'Nginx Full'

# CMD ["systemctl", "start", "nginx"]

RUN apt-get install python3.10 -y
RUN apt install python3-pip -y
# RUN snap install core
# RUN snap refresh core
# RUN snap install --classic certbot
# RUN pip install -U pip

RUN apt-get install python3-openssl -y

# RUN pip install pyOpenSSL

# Remove any existing config files
# RUN rm /etc/nginx/conf.d/*
# RUN rm /etc/nginx/nginx.conf

# RUN openssl req -x509 -nodes -days 365 -newkey rsa:2048 -keyout /etc/ssl/private/selfsigned.key -out /etc/ssl/certs/selfsigned.crt

# RUN rm -f /etc/nginx/sites-enabled/default
# RUN unlink /etc/nginx/sites-enabled/default

# Copy the custom Nginx configuration
COPY /services/etc/nginx/nginx.conf /etc/nginx/nginx.conf

# Certificates

COPY /services/etc/nginx/certificate/selfsigned.key /etc/ssl/private/
COPY /services/etc/nginx/certificate/selfsigned.crt /etc/ssl/certs/



COPY /services/etc/nginx/sites-available/reverse-proxy.conf /etc/nginx/sites-available/reverse-proxy.conf

RUN mkdir etc/nginx/sites-enabled
RUN ln -s /etc/nginx/sites-available/reverse-proxy.conf /etc/nginx/sites-enabled/

# Expose port 80 for Nginx
EXPOSE 80 443