#remove everything that was built before
docker stop $(docker ps -a -q)
docker rm $(docker ps -a -q)

#start building
docker-compose build
docker-compose up

