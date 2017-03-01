FROM actuino/python2-unicorn-armhf:1
WORKDIR /root/

ENV UNICORN_CLIENT_NAME "Display1"

COPY client.py ./
COPY *.json ./

RUN pip install socketIO-client

CMD ["python","client.py"]