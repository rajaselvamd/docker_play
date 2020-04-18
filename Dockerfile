# pull basic ubuntu image
FROM ubuntu

# contact 
LABEL maintainer="rajaselvam@gmail.com"

# get python related libraries to the container
RUN apt-get update
RUN apt-get -y install python
RUN apt-get -y install python-setuptools
RUN apt-get -y install python-pip
RUN pip install requests

# copy localy python file to container
COPY org_find_for_mac.py /tmp/org_find_for_mac.py 

# run the python script in container
ENTRYPOINT ["python", "/tmp/org_find_for_mac.py"]
