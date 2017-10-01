FROM node:8.6

RUN apt-get update
RUN apt-get install python-pip python-dev -y
RUN pip install virtualenv

ADD . /code
WORKDIR /code
CMD ["./run.sh"]
