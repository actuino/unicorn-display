/**
 * A Simple Web and WebSocket server with NodeJS
 * actuino/unicorn-display
 * @actuino
 */

// Port number to listen on
var SERVER_PORT = 80;

var http = require('http');
var querystring = require('querystring');
var fs = require('fs');

var digits = JSON.parse(fs.readFileSync('./web/res/digits.json'));
var empty = JSON.parse(fs.readFileSync('./web/res/empty.json'));


var server = http.createServer(function(req, res) {
    console.log(req.url);
    if (req.method == 'POST') {
        if (req.url == '/display/') {
            var jsonString = '';
            req.on('data', function(data) {
                jsonString += data;
                if (jsonString.length > 1e6) {
                    jsonString = "";
                    res.writeHead(413, {
                        'Content-Type': 'text/plain'
                    });
                    res.end();
                    req.connection.destroy();
                }
            });
            req.on('end', function() {
                try {
                    var data = JSON.parse(jsonString);

                    console.log(data);
                    //console.log(data.Payload);
                    sendIt(data);
                    res.writeHead(200, "OK", {
                        'Content-Type': 'text/plain'
                    });
                    res.end();
                }
                catch (e) {
                    console.log('No Json');
                    res.writeHead(400, "No JSON", {
                        'Content-Type': 'text/plain'
                    });
                    res.end();
                }
            });
        }
    };

    if (req.method == 'GET') {
        if (req.url == '/') {
            req.url = '/index.html'
        }
        if (fs.existsSync('./web/' + req.url)) {
            fs.readFile('./web/' + req.url, 'utf-8', function(error, content) {
                res.writeHead(200, {
                    "Content-Type": "text/html"
                });
                res.end(content);
            });

        }
        else {
            res.writeHead(404, "Not found", {
                'Content-Type': 'text/plain'
            });
            res.end();
        }
    }
});


// socket.io

var io = require('socket.io').listen(server);

var Session = require("express-session");
var FileStore = require('session-file-store')(Session);

var session = Session({
    secret: "uni34disp43",
    resave: true,
    saveUninitialized: true,
    store: new FileStore({
        path: ".store"
    })
});

var sharedsession = require("express-socket.io-session");

io.use(sharedsession(session, {
    autoSave: true,

}));

// Log client connection to the console

io.sockets.on('connection', function(socket) {
    console.log('Client connection');
    socket.handshake.session.val = 50;
    socket.handshake.session.save();
    socket.on('message', function(message) {
        console.log('Got message from client : ' + message);
    });
    socket.on('name', function(message) {
        console.log('Got Name ' + message);
        socket.handshake.session.name = message;
        socket.handshake.session.save();
        socket.broadcast.emit('message', message + ' Connected');
    });
    socket.on('previous', function(message) {
        console.log('Got Previous');
        socket.handshake.session.val--;
        socket.handshake.session.save();
        socket.broadcast.emit('previous', socket.handshake.session.name + ' : ' + socket.handshake.session.val);
        message = int2message(socket.handshake.session.val);
        socket.broadcast.emit('file', message);
    });
    socket.on('next', function(message) {
        console.log('Got Next');
        socket.handshake.session.val++;
        socket.handshake.session.save();
        socket.broadcast.emit('next', socket.handshake.session.name + ' : ' + socket.handshake.session.val);
        message = int2message(socket.handshake.session.val);
        socket.broadcast.emit('file', message);
    });
    socket.on('set', function(message) {
        console.log('Got Set');
        console.log(message);
        socket.broadcast.emit('file', message);
    });
    socket.on('nextPage', function(message) {
        console.log('Got Next Page');
        socket.broadcast.emit('nextPage');
    });
    socket.on('previousPage', function(message) {
        console.log('Got Previous Page');
        socket.broadcast.emit('previousPage');
    });
});





server.listen(SERVER_PORT);


function sendIt(data) {
    io.sockets.emit('file', data);
}

function int2message(n) {
    var message = empty;
    if (n > 99) {
        n = 0;
    }
    if (n < 0) {
        n = 0;
    }
    var d = Math.floor(n / 10);
    var u = n - d * 10;
    //console.log(d, u);
    for (var l = 0; l <= 3; l++) {
        for (var c = 0; c <= 2; c++) {
            message["Payload"][l][c] = digits[d][l][c];
            message["Payload"][l][c + 4] = digits[u][l][c];
        }
    }
    message["Channel"] = "Editor";
    console.log(message);
    return message;
}
