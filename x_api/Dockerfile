FROM ubuntu:latest

RUN     apt-get -y update; \
        apt-get -y install python3; \
        apt-get -y install python3-pip;

COPY    flask_app.py        /opt/source-code/
COPY    env_variables.py    /opt/source-code/

COPY    requirements.txt /tmp/requirements.txt

RUN     pip3 install --no-cache -r /tmp/requirements.txt

ENV FLASK_APP=/opt/source-code/flask_app.py
ENV FLASK_ENV=development
ENV FLASK_DEBUG=1

EXPOSE  8001

ENTRYPOINT python3 /opt/source-code/flask_app.py run