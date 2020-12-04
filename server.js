const express = require('express');
const app = express();
var path = require('path');
require('dotenv').config();
const port = process.env.PORT || 3000;
app.use(express.static(path.join(__dirname, 'public')));
app.use('/', require('./route/price'));
app.listen(port, (req, res) => {
    console.log(`server start on port ${port}`)
})
