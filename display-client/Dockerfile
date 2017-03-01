FROM actuino/python2-unicorn-armhf:1
WORKDIR /root/

ENV UNICORN_CLIENT_NAME "Display1"
ENV UNICORN_SERVER_HOST "192.168.7.3"
ENV UNICORN_SERVER_PORT 80

COPY client.py ./
COPY *.json ./

RUN pip install socketIO-client

CMD ["python","client.py"]