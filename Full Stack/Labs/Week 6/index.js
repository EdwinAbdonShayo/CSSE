var express = require('express');
var app = express();
var port = 3553;

// Here

// Middleware to parse URL-encoded bodies (not strictly necessary for query params but useful)
app.use(express.urlencoded({ extended: true }));

app.get('/', (req, res) => {
    const paramName = req.query.name; // Accessing a query parameter named 'name'
    const paramAge = req.query.age; // Accessing a query parameter named 'age'

    if (paramName && paramAge) {
        res.send(`Hello, ${paramName}! You are ${paramAge} years old.`);
    } else {
        res.send('Hello, World! (Provide?name=YourName&age=YourAge in the URL)');
    }
});

app.listen(port, () => {
    console.log(`Server running on port ${port}`);
});