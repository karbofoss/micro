/usr/local/bin/docker-compose build
/usr/local/bin/docker-compose run web2 bash -c ./restore.sh
/usr/local/bin/docker-compose run web1 bash -c ./restore.sh
/usr/local/bin/docker-compose up
