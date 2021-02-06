const express = require('express');
const app = express();
var path = require('path');
const ejs = require("ejs");
require('./cron')
require('dotenv').config();
require('./helpers/init_mogodb')
app.set('view engine', 'ejs');
app.set('views', path.join(__dirname, 'views'));
app.use(express.static(path.resolve(__dirname, 'assets')));
app.use(express.static(path.join(__dirname, 'public')));
app.use('img', express.static(path.join(__dirname, 'public/img')))
app.use('js', express.static(path.join(__dirname, 'public/js')))
app.use('css', express.static(path.join(__dirname, 'public/css')))
app.use('vendor', express.static(path.join(__dirname, 'public/vendor')))
app.use('fonts', express.static(path.join(__dirname, 'public/fonts')))


app.use('/', require('./route/index'));
const port = process.env.PORT || 3000;
app.listen(port, (req, res) => {
  console.log(`server start on port ${port}`)
})
