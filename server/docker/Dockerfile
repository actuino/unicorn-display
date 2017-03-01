FROM alexellis2/nodejs-armv6:4.4
WORKDIR /root/

EXPOSE 80
ENV UNICORN_SERVER_NAME ""

COPY ../server.js ./
COPY ../README.md ./
COPY ../package.json ./
COPY ../web web

RUN npm install

CMD ["node server.js"]