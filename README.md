# Eye_Segmentation_app

## Docker

You need to have Docker to use this repository.

If you have any issue regarding docker here is a [quick setup](https://github.com/Shifoue/Eye_Segmentation_app/blob/main/Docker.md).

## Setup

Clone the repository :
```
git clone https://github.com/Shifoue/Eye_Segmentation_app.git
```

If you don't have openssl here is how to install it :
```
sudo apt-get update
sudo apt-get install openssl
```


Go to the root of the Eye_Segmentation_app repository and generate the self signed cerificate :
```
mkdir services/etc/nginx/certificate

openssl req -x509 -nodes -days 365 -newkey rsa:2048 -keyout services/etc/nginx/certificate/selfsigned.key -out services/etc/nginx/certificate/selfsigned.crt
```
This certificate will be valid for 365 days. You can replace it by your own, just put them inside the repository services/etc/nginx/certificate/.


Now that everything is setup just run :
```
docker compose up -d
```


Once it is finished you can check that you have 2 containers by using the ```docker ps``` command :
  - ```eye_segmenation_app-web_app``` which is the container containing the eye segmentation model
  - ```eye_segmenation_app-nginx``` which is the reverse proxy.


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

If you don't want to remove all docker volumes and images remove the ```-a``` option

## Configuration files

If you wish you can modify the following configuration files for the reverse proxy server:
  - [The proxy server configuration](https://github.com/Shifoue/Eye_Segmentation_app/blob/main/services/etc/nginx/default.conf)
  - [The reverse proxy configuration](https://github.com/Shifoue/Eye_Segmentation_app/blob/main/services/etc/nginx/includes/reverse_proxy.conf)
  - [The ssl configuration](https://github.com/Shifoue/Eye_Segmentation_app/blob/main/services/etc/nginx/includes/ssl.conf)
