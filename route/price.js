const express = require('express')
const routes = express.Router()
const axios = require('axios');
const cheerio = require('cheerio');
axios.get('https://www.indianspices.com/marketing/price/domestic/daily-price.html')
    .then((res) => {
        const $ = cheerio.load(res.data,);
        let list = [];
        $('table')
            .each((index, element) =>
                list.push($(element).html()))
        routes.get('/', function (req, res) {
            res.send( `<table>${list[1]}</table>` );   
        })
    })
module.exports = routes