FROM ubuntu:latest

RUN     apt-get -y update; \
        apt-get -y install python3; \
        apt-get -y install python3-pip;

COPY    flask_app.py    /opt/source-code/
COPY    templates/*     /opt/source-code/templates/
COPY    static/css/*    /opt/source-code/static/css/
COPY    static/*.png    /opt/source-code/static/
COPY    static/*.js     /opt/source-code/static/       
COPY    static/*.svg    /opt/source-code/static/

COPY    requirements.txt /tmp/requirements.txt

RUN     pip3 install --no-cache -r /tmp/requirements.txt

ENV FLASK_APP=/opt/source-code/flask_app.py
ENV FLASK_ENV=development
ENV FLASK_DEBUG=1

EXPOSE  8000

ENTRYPOINT python3 /opt/source-code/flask_app.py run