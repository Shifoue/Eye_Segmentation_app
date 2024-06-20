FROM nginx:latest

COPY services/etc/nginx/default.conf /etc/nginx/conf.d/default.conf
COPY services/etc/nginx/html/page-not-found.html /var/www/html/page-not-found.html
COPY services/etc/nginx/includes/ /etc/nginx/includes/
COPY services/etc/nginx/certificate/selfsigned.key /etc/ssl/certs/nginx/
COPY services/etc/nginx/certificate/selfsigned.crt /etc/ssl/certs/nginx/