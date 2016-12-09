# Demonstration of service interaction
## Prerequisites
- docker
- docker-compose

## Installation on Amazon EC2 Linux Ubuntu 16.04
In Security Groups for EC2 create rules to enable access on 8881, 8882 ports. Start ssh session.
```
sudo apt update
sudo apt install -y git-core
cd /home/ubuntu
git clone https://github.com/imentali/micro
cd micro
sudo chmod +x build_run.sh
sudo ./build_run.sh
```
Check logs. Close docker-compose.
```
Ctrl-C
```
Create file  /lib/systemd/system/test_webservice.service
```
[Unit]
Description=Test webservice container
Requires=docker.service
After=docker.service

[Service]
Restart=always
ExecStart=/usr/local/bin/docker-compose -f /home/ubuntu/micro/docker-compose.yml up
ExecStop=/usr/local/bin/docker-compose -f /home/ubuntu/micro/docker-compose.yml stop

[Install]
WantedBy=multi-user.target
Alias=webservice.service
```
sudo systemctl enable test_webservice.service
Reboot
