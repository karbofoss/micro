sudo /usr/local/bin/docker-compose stop web1
sudo /usr/local/bin/docker-compose stop web2
sudo /usr/local/bin/docker-compose stop db1
sudo /usr/local/bin/docker-compose stop db2
sudo /usr/local/bin/docker-compose rm -f web1
sudo /usr/local/bin/docker-compose rm -f web2
sudo /usr/local/bin/docker-compose rm -f db1
sudo /usr/local/bin/docker-compose rm -f db2

#sudo service docker stop
#sudo rm -rf /var/lib/docker
#sudo rm -rf log1
#sudo rm -rf log2
#sudo rm -rf pgdata1
#sudo rm -rf pgdata2
#sudo service docker start
