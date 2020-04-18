## docker_play
Generic repository for docker related sample projects

# Find Vendor Name for a MAC Address
This is a sample Docker to find Vendor Name from a MAC Address. The Docker contains Ubuntu base and a python script to query url https://macaddress.io for vendor details and show the vendor name if found.
The python script is using standard python libraries “requests” for url query and “re” for mac-address validation.

## Getting Started
This sample docker image creation had done under Ubuntu 16.06 LTS server. 

## Prerequisites
- Reachability of Docker repository and Ubuntu repository
- Ubuntu - Docker will pull the base ubuntu and update required libraries
- Python - Docker will install the python libraries under ubuntu 
- sudo - may not need if user has root priviledge

## Setup docker repository
```
sudo apt-get update
sudo apt-get install apt-transport-https ca-certificates curl software-properties-common
curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo apt-key add -
sudo add-apt-repository "deb [arch=amd64] https://download.docker.com/linux/ubuntu $(lsb_release -cs) stable"
```
## Install Docker CE
```
sudo apt-get update
sudo apt-get install docker-ce
```
## Verify Docker installation
```
sudo docker run hello-world
```
## Check the Docker images
```
sudo docker images
```
**Here the actual task starts.** 

## Create python script

Create the python script, run and verify the output
```
python org_find_for_mac.py 08:CC:68:11:11:11
```
**Output:**
Company Name for mac 08:CC:68:11:11:11 is Cisco Systems, Inc

## Create Dockerfile
Create a folder(optional) and create a startup file name for docker, which is "Dockerfile" and add the list of commands.

## Create docker build
```
sudo docker build -t <build tag name> .
```
Once received the successful built message, check the docker image list
```
sudo docker images
```
## Docker run
```
sudo docker run <docker image id> <mac-address>
sudo docker run -ti <docker build repo name> <mac-address>
```
Sample run:
```
sudo docker run edfb602ba3c7 08:CC:68:11:11:11
```
## Output
  Company Name for mac 08:CC:68:11:11:11 is Cisco Systems, Inc

