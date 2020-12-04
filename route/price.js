const express = require('express')
const routes = express.Router()
const axios = require('axios');
const cheerio = require('cheerio');
// axios.get('https://www.indianspices.com/marketing/price/domestic/daily-price.html')
//     .then((res) => {
//         const $ = cheerio.load(res.data,);
//         let list = [];
//         $('table')
//             .each((index, element) =>
//                 list.push($(element).html()))
//         routes.get('/', function (req, res) {
//             res.send( `<h1>BY Abin</h1><br><table>${list[1]}</table>` );   
//         })
//     })

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
    res.send(`<br><table>${list[1]}</table>
           <br>
           <h1>BY Abin</h1>
           <p>
           <b>
           Github   :<a href="https://github.com/abjs">abjs</a><br>
           Facebook :<a href="https://www.facebook.com/itsmeabjs.me"> Abin Jooseph</a><br>
           Insagram :<a href="http://www.insagram.com/itsmeabjs">itsmeabjs</a><br>
           </b>
           <p>` );

})


module.exports = routes
