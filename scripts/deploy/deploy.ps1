docker-compose -f "docker-compose.yml" down
docker image rm test_app_app

docker-compose -f "docker-compose.yml" up -d --build
