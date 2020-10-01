# Docker
https://docs.docker.com/engine/install/debian/
https://www.docker.com/blog/happy-pi-day-docker-raspberry-pi/

sudo apt-get install apt-transport-https ca-certificates software-properties-common -y

curl -fsSL get.docker.com -o get-docker.sh && sh get-docker.sh

sudo usermod -aG docker pi

sudo curl https://download.docker.com/linux/raspbian/gpg

sudo nano /etc/apt/sources.list

deb https://download.docker.com/linux/raspbian/ buster stable

ctrl+X Y Enter

sudo apt update && sudo apt -y upgrade

sudo systemctl start docker.service

docker info

sudo apt install docker-compose