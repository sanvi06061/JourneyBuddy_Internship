const express = require("express");

const app = express();

const PORT = 3000;

// Middleware / Interceptor
function requestLogger(req, res, next) {
    const timestamp = new Date().toISOString();

    console.log("----- Incoming Request -----");
    console.log("Timestamp:", timestamp);
    console.log("Method:", req.method);
    console.log("URL:", req.originalUrl);
    console.log("User-Agent:", req.headers["user-agent"]);
    console.log("Parameters:", req.query);

    next();
}

// Apply middleware
app.use(requestLogger);

// Informational route
app.get("/info", (req, res) => {
    res.json({
        message: "This is the informational route"
    });
});

app.listen(PORT, () => {
    console.log(`Server running at http://localhost:${PORT}`);
});