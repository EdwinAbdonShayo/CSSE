const http = require('http');
const express = require('express');
const lodas = require('lodash');

const lessons = [
    { 'topic': 'math', 'location': 'London', 'price': 100 },
    { 'topic': 'math', 'location': 'Liverpool', 'price': 80 },
    { 'topic': 'math', 'location': 'Ocford', 'price': 90 },
    { 'topic': 'math', 'location': 'Bristol', 'price': 120 },
];



const PORT = 3000;

// Create the server
const server = http.createServer((req, res) => {

    const url = req.url;
    res.setHeader('Content-Type', 'application/json');

   // Handle incoming requests
    if (req.url === '/' && req.method === 'GET') {
        res.writeHead(200); 
        res.end('Hello, Babu!\n'); 
    } else {
        res.writeHead(404); 
        res.end('404 Not Found\n'); 
    }
});

server.listen(PORT, () => {
    console.log(`Server is running at http://localhost:${PORT}`);
});
