#Main image project based 
FROM python:3.11
RUN apt-get update && apt-get install
#Means Python will not try to write .pyc files
ENV PYTHONUNBUFFERED 1
#Ensures our console output is not buffered by Docker
ENV PYTHONDONTWRITEBYTECODE 1
#Thats create the main path that we will work on it
RUN mkdir /code
WORKDIR /code
#Copy the file what contains the primary python dependencies of the project
COPY requirements.txt /code/
#Update the python pip library
RUN python -m pip install --upgrade pip
#Intall the dependencies
RUN python -m pip install -r requirements.txt
#Copy the root directory of the project to the root code directory in our container 
COPY . /code/
#Copy the shell file which contains the primordial django commands
COPY docker-entrypoint.sh /
#ENTRYPOINT [ "sh","docker-entrypoint.sh" ]


#This executes the django project in a gunicorn deploy method
CMD ["gunicorn", "-c", "config/gunicorn/conf.py", "--bind", ":8000", "--chdir", "fireborn", "fireborn.wsgi:application"]
