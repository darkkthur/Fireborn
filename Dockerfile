#Main image project based 
FROM python:3.11
RUN apt-get update && apt-get install
#Means Python will not try to write .pyc files
ENV PYTHONUNBUFFERED 1
#Ensures our console output is not buffered by Docker
ENV PYTHONDONTWRITEBYTECODE 1
RUN mkdir /code
WORKDIR /code
COPY requirements.txt /code/
RUN python -m pip install --upgrade pip
RUN python -m pip install -r requirements.txt
COPY . /code/
COPY docker-entrypoint.sh /


#ENTRYPOINT [ "sh","docker-entrypoint.sh" ]
CMD ["gunicorn", "-c", "config/gunicorn/conf.py", "--bind", ":8000", "--chdir", "fireborn", "fireborn.wsgi:application"]
