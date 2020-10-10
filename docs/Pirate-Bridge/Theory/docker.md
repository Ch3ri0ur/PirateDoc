# Docker

Docker allows to Run Docker Container which contain pre compiled code and are mostly not bound to any OS. It is similar to a VM, but the Docker Container is not an OS and can be adjusted so that Processes inside can access the Hostsystem.
https://www.docker.com/why-docker
https://docs.docker.com/engine/install/debian/
https://www.docker.com/blog/happy-pi-day-docker-raspberry-pi/

## Docker Installation
### Requirements
```
sudo apt-get install apt-transport-https ca-certificates software-properties-common -y
```

### Download Script for easy installation
```
curl -fsSL get.docker.com -o get-docker.sh && sh get-docker.sh
```

### Add pi-User to Docker to allow starting without sudo rechten 
```
sudo usermod -aG docker pi
```

### Add Docker to Source.list for easy update and upgrade
Get Docker Public Key for Raspbian Docker Version
```
sudo curl https://download.docker.com/linux/raspbian/gpg
```
Open Source.list to add Source Path for the Docker Software
```
sudo nano /etc/apt/sources.list
```
Add to Source path to the File
```
deb https://download.docker.com/linux/raspbian/ buster stable
```
Use ```CTRL + X``` to close the Editor and ```Y``` and than ```Enter``` to Save Changes

Perform an Update and Upgrade
```
sudo apt update && sudo apt -y upgrade
```

### Start Docker Service
```
sudo systemctl start docker.service
```


### Install Docker Compose that manages the Docker container
```
sudo apt install docker-compose -y
```

## Useful Docker Commands

### Display Info about Docker installation and Running Container
```
sudo docker info
```