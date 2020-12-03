const express = require('express');
const app = express();
require('dotenv').config();
const port = process.env.PORT || 3000;
app.use('/', require('./route/price'));
app.listen(port, (req, res) => {
    console.log(`server start on port ${port}`)
})