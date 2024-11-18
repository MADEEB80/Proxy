const express = require('express');
const { createProxyMiddleware } = require('http-proxy-middleware');
const bodyParser = require('body-parser');
const axios = require('axios');
const HttpsProxyAgent = require('https-proxy-agent');

// Proxy credentials
const proxyUrl = 'http://9cb7911bc7dce412c1bd__cr.us:e3d1e6433ed3da7c@gw.dataimpulse.com:823';
const proxyAgent = new HttpsProxyAgent(proxyUrl);

// Create Express server
const app = express();
const PORT = 8080;

// Middleware
app.use(bodyParser.json());
app.use(bodyParser.urlencoded({ extended: true }));

// Test Proxy - Fetch Public IP
app.get('/get-ip', async (req, res) => {
    try {
        const response = await axios.get('https://api.ipify.org?format=json', { httpsAgent: proxyAgent });
        res.json({ success: true, ip: response.data.ip });
    } catch (error) {
        res.status(500).json({ success: false, message: 'Proxy failed', error: error.message });
    }
});

// Proxy Middleware for Custom Websites
app.use('/proxy', createProxyMiddleware({
    target: 'http://example.com', // Default target if not specified
    changeOrigin: true,
    secure: false,
    agent: proxyAgent,
    router: (req) => {
        const target = req.query.target; // Read target URL from query string
        return target || 'http://example.com'; // Default to example.com if not provided
    },
    logLevel: 'debug', // Debugging logs
}));

// Start the server
app.listen(PORT, () => {
    console.log(`Proxy server running at http://localhost:${PORT}`);
});
