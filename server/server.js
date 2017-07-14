/**
 * A Simple Web and WebSocket server with NodeJS
 * actuino/unicorn-display
 * @actuino
 */

const VER = '1.0.1';



var http = require('http');
var querystring = require('querystring');
var fs = require('fs');

var digits = JSON.parse(fs.readFileSync('./web/res/digits.json'));
var empty = JSON.parse(fs.readFileSync('./web/res/empty.json'));

var config = JSON.parse(fs.readFileSync('./web/config.json'));
config.VER = VER;
fs.writeFile('./web/config.json', JSON.stringify(config), 'utf8');


var server = http.createServer(function(req, res) {
    console.log(req.url);
    if (req.method == 'POST') {
        if (req.url == '/display/' || req.url == '/command/') {
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
                    console.log(req.url);
                    //console.log(data.Payload);
                    if (req.url == '/display/') {
                        sendIt(data);
                    }
                    if (req.url == '/command/') {
                        command(data);
                    }
                    res.writeHead(200, "OK", {
                        'Content-Type': 'text/plain'
                    });
                    res.end();
                }
                catch (e) {
                    console.log('No Json');
                    console.log(jsonString);
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

// Log client connection in console

io.sockets.on('connection', function(socket) {
    console.log('Client connection');
    socket.handshake.session.val = 50;
    socket.handshake.session.save();
    socket.on('message', function(message) {
        console.log('Got message from client : ' + message);
    });
    socket.on('name', function(message) {
        console.log('Got Name ' + message);
        try {
            socket.handshake.session.name = JSON.parse(message); // Name, Serial
            socket.handshake.session.save();
        }
        catch (e) {}
        socket.broadcast.emit('message', message + ' Connected');
    });
    socket.on('page', function(message) {
        console.log('Got Page ' + message);
        // TODO : transmit to editor
        sendToName('page', 'Editor', message);
    });
    // Should disappear
    socket.on('previous', function(message) {
        console.log('Got Previous');
        socket.handshake.session.val--;
        socket.handshake.session.save();
        //socket.broadcast.emit('previous', socket.handshake.session.name + ' : ' + socket.handshake.session.val);
        message = int2message(socket.handshake.session.val);
        socket.broadcast.emit('file', message);
    });
    // Should disappear
    socket.on('next', function(message) {
        console.log('Got Next');
        socket.handshake.session.val++;
        socket.handshake.session.save();
        //socket.broadcast.emit('next', socket.handshake.session.name + ' : ' + socket.handshake.session.val);
        message = int2message(socket.handshake.session.val);
        socket.broadcast.emit('file', message);
    });
    socket.on('set', function(message) {
        console.log('Got Set');
        console.log(message);
        socket.broadcast.emit('file', message);
    });
    socket.on('command', function(message) {
        console.log('Got Command');
        console.log(message);
        //socket.broadcast.emit('command', message);
        sendToName('command', message["Name"], message);
    });

});





server.listen(8080);


// sends a command to the matching clients
// TODO : match on serial also
function sendToName(command, name, message) {
    console.log("sendToName " + name + " " + command + " " + message)
    for (var i in io.sockets.connected) {
        var s = io.sockets.connected[i];
        try {
            //console.log(s.handshake.session);
            if (s.handshake.session.name != undefined) {
                //console.log(s.handshake.session.name["Name"]);
                if (s.handshake.session.name["Name"] == name) {
                    s.emit(command, message)
                    console.log("Transmited to " + name)
                }
            }
        }
        catch (e) {}
    }

}

// Sends a data payload to everyone
function sendIt(data) {
    if (64 == data.Payload.length) {
        // slice in 8x8
        data.Payload = data.Payload.chunk(8);
    }
    io.sockets.emit('file', data);
}


// Sends a command to the matching display
function command(data) {
    var destName = 'Astra';
    /*if ('Sky1' == data.Name) {
        destName = 'Layji';
        data.Name = 'Layji';
    }*/
    sendToName('command', destName, data);
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

Object.defineProperty(Array.prototype, 'chunk', {
    value: function(chunkSize) {
        var R = [];
        for (var i = 0; i < this.length; i += chunkSize)
            R.push(this.slice(i, i + chunkSize));
        return R;
    }
});
