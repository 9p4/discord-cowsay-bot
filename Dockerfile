# set base image (host OS)
FROM python:3.9

# set the working directory in the container
WORKDIR /code

# copy the dependencies file to the working directory
COPY requirements.txt .

# install dependencies
RUN pip install -r requirements.txt

# copy the required files to the working directory
COPY discord-cowsay.py .
COPY cowsay.py .

# command to run on container start
CMD [ "python", "./discord-cowsay.py" ] 
