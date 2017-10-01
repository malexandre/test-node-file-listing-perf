FROM node:8.6

RUN apt-get update
RUN apt-get install python-pip python-dev -y

ADD . /code
WORKDIR /code
CMD ["./run.sh"]
