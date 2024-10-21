var express =  require("express");
var http = require("http");
var path = require("path");
var fs = require("fs");

var app = express();

app.use(function(req, res) {
    console.log("In comes a request to: " + req.url);
    res.end("Hello World!");
});

http.createServer(app).listen(3300);