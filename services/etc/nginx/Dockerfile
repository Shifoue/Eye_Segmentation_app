FROM nginx:latest
# Remove any existing config files
RUN rm /etc/nginx/conf.d/*
# Copy the custom Nginx configuration
COPY /services/etc/nginx/nginx.conf /etc/nginx/conf.d/
# Expose port 80 for Nginx
EXPOSE 80