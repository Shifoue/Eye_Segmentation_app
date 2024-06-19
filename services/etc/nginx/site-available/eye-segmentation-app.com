# /etc/nginx/eye-segmentation-app.com

# Redirect www.eye-segmentation-app.com to eye-segmentation-app.com
server {
        server_name www.eye-segmentation-app.com;
        rewrite ^ http://eye-segmentation-app.com/ permanent;
}

# Handle requests to eye-segmentation-app.com on port 80
server {
        listen 80;
        server_name eye-segmentation-app.com;

                # Handle all locations
        location / {
                        # Pass the request to Gunicorn
                proxy_pass http://127.0.0.1:5000;

                # Set some HTTP headers so that our app knows where the
                # request really came from
                proxy_set_header Host $host;
                proxy_set_header X-Real-IP $remote_addr;
                proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
        }
}
