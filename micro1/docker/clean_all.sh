/usr/local/bin/docker-compose stop web1
/usr/local/bin/docker-compose stop web2
/usr/local/bin/docker-compose stop db1
/usr/local/bin/docker-compose stop db2
/usr/local/bin/docker-compose rm -f web1
/usr/local/bin/docker-compose rm -f web2
/usr/local/bin/docker-compose rm -f db1
/usr/local/bin/docker-compose rm -f db2

#docker rm $(docker ps -a -q)
#docker rmi $(docker images -q)

