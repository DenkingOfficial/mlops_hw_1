#!/bin/sh
printf "DockerHub username: "
read -r USERNAME
printf "DockerHub password: "
stty -echo
read -r PASSWORD
stty echo

APP_NAME="cat_breed_classifier"
TAG=$(git rev-parse --abbrev-ref HEAD)_$(git rev-parse --short HEAD)
APP="$USERNAME/$APP_NAME:$TAG"

docker login -u $USERNAME -p $PASSWORD
docker-compose build
docker tag $APP_NAME $APP
docker image rm $APP_NAME
docker push $APP
docker run -p 8000:8000 $APP
