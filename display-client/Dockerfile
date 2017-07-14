FROM actuino/python2-unicorn-armhf:2
WORKDIR /root/

ENV UNICORN_CLIENT_NAME "Astra"
ENV UNICORN_SERVER_HOST "localhost"
ENV UNICORN_SERVER_PORT 80

COPY *.py ./
COPY channels channels
COPY classes classes
COPY effects effects
copy local local
copy res res

RUN pip install socketIO-client

CMD ["python","client.py"]
