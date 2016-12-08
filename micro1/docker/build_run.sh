sudo /usr/local/bin/docker-compose build
#sudo /usr/local/bin/docker-compose run db1 ls
#sudo /usr/local/bin/docker-compose run db2 ls
sudo /usr/local/bin/docker-compose run web2 bash -c ./restore.sh
sudo /usr/local/bin/docker-compose run web1 bash -c ./restore.sh
sudo /usr/local/bin/docker-compose up
