cd micro1
git reset --hard HEAD
git pull
cp docker-compose.yml ..
cd ..
cd micro2
git reset --hard HEAD
git pull
cd ..
cp micro1/docker/* .
# sudo docker-compose build && sudo docker-compose up
