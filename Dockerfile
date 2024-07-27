#Using a python image from the docker hub
FROM python:3.12-slim

# Set the working directory in the container
WORKDIR /app

# Copy all the current directory content into the container at /app
COPY . /app

#Install any needed packages specified in requirement.txt
RUN pip install -r requirement.txt

#EXPOSE  5000 5001 5002 5003
EXPOSE 3000

CMD python jinja_temp.py

