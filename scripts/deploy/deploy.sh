docker-compose -f "docker-compose.yml" down
docker image rm nginx
docker image rm nt_app

docker-compose -f "docker-compose.yml" up -d --build