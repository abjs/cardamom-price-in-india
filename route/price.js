const express = require('express')
const routes = express.Router()
const axios = require('axios');
const cheerio = require('cheerio');
const fetchData = async (siteUrl) => {
    const result = await axios.get(siteUrl);
    return cheerio.load(result.data);
};
url = 'https://www.indianspices.com/marketing/price/domestic/daily-price.html'
routes.get('', async (req, res) => {
    const $ = await fetchData(url);
    let list = [];

    $('table')
        .each((index, element) =>
            list.push($(element).html()))
    res.send(`
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="google-site-verification" content="d2vem5q5DGNV7EWjIUEz8LZUT8XqkNgVwj35Q_DYabo" />
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <meta name="title" content="Cardamom Price Today">
        <meta name="description" content="Hear you can find Cardamom Price of every day in kerala">
        <meta name="keywords" content="Cardamom Price,elakka price,Cardamom,elakka,price of Cardamom,elakka price,Cardamom Price Today,cardamom price today in kerala,cardamom price per kg">
        <meta name="robots" content="index, follow">
        <meta http-equiv="Content-Type" content="text/html; charset=utf-8">
        <meta name="language" content="English">
        <meta name="revisit-after" content="1 days">
        <meta name="author" content="Abin Joseph">
        <title>Cardamom Price Today</title>
    </head>
    <body>
         <table>
             ${list[1]}
        </table>
        <br>
        <h3>By Abin</h3>
        <p>
        <b>
        Github   :<a href="https://github.com/abjs">abjs</a><br>
        Facebook :<a href="https://www.facebook.com/itsmeabjs.me"> Abin Jooseph</a><br>
        Insagram :<a href="http://www.insagram.com/itsmeabjs">itsmeabjs</a><br>
        </b>
        <p> 
    </body>
    </html>
    `    
    );

})
module.exports = routes
