FROM nginx:latest
# Remove any existing config files
RUN rm /etc/nginx/conf.d/*
RUN rm -f /etc/nginx/sites-enabled/default
# Copy the custom Nginx configuration
COPY /services/etc/nginx/nginx.conf /etc/nginx/conf.d/

# COPY /services/etc/nginx/sites-available/reverse-proxy.conf /etc/nginx/sites-available/reverse-proxy.conf

# # Expose port 80 for Nginx

# RUN ln -s /services/etc/nginx/sites-available/reverse-proxy.conf /services/etc/nginx/sites-enabled/

EXPOSE 80