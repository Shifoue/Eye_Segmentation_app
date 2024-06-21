# Eye_Segmentation_app

## Install Docker

```
# Add Docker's official GPG key:
sudo apt-get update
sudo apt-get install ca-certificates curl
sudo install -m 0755 -d /etc/apt/keyrings
sudo curl -fsSL https://download.docker.com/linux/ubuntu/gpg -o /etc/apt/keyrings/docker.asc
sudo chmod a+r /etc/apt/keyrings/docker.asc

# Add the repository to Apt sources:
echo \
  "deb [arch=$(dpkg --print-architecture) signed-by=/etc/apt/keyrings/docker.asc] https://download.docker.com/linux/ubuntu \
  $(. /etc/os-release && echo "$VERSION_CODENAME") stable" | \
  sudo tee /etc/apt/sources.list.d/docker.list > /dev/null
sudo apt-get update
```

```
sudo apt-get install docker-ce docker-ce-cli containerd.io docker-buildx-plugin docker-compose-plugin
```

```
sudo docker run hello-world
```

```
sudo chmod 666 /var/run/docker.sock
```

## Setup

Clone the repository :
```
git clone https://github.com/Shifoue/Eye_Segmentation_app.git
```

Go to the root of the Eye_Segmentation_app repository and generate the self signed cerificate, if you don't have openssl you might need to install it :
```
mkdir services/etc/nginx/certificate

openssl req -x509 -nodes -days 365 -newkey rsa:2048 -keyout services/etc/nginx/certificate/selfsigned.key -out services/etc/nginx/certificate/selfsigned.crt
```
This certificate will be valid for 365 days. You can replace it certificate by your own, just put them inside the repository services/etc/nginx/certificate/.

Now that everything is setup just run :
```
docker compose up -d
```

Once it is finished you can check that you have 2 containers :
  - eye_segmenation_app-web_app which is the container containing the eye segmentation model
  - eye_segmenation_app-nginx which is the reverse proxy.

To test your server connect to https://HOST_NAME.com

## Docker clean up

```
docker ps
docker stop ID
```
Where ID is the container ID of the container you want to stop.

Then you can clean up using the following commands :
```
docker system prune -a --volumes
docker volume prune -a
docker images -a
```
