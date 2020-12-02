const express = require('express')
const routes = express.Router()
const axios = require('axios');
const cheerio = require('cheerio');
axios.get('https://www.indianspices.com/marketing/price/domestic/daily-price.html')
    .then((res) => {
        const $ = cheerio.load(res.data);
        // // console.log(res.data);
        // console.log($('.tabstable')
        // .html())
       list = [];
       const fust =$('.tabstable').html()
    //    list.push(fust)
     
       $('.tabstable')
       .each((index,element)=>
        list.push( $(element).html())
        
       ) 
       const last =$('.tabstable').last().html()
           list.push(last)   
    // let y =$('.tabstable').each().element().html()
    const final =list[1];
    // var ast = HTML.parse(final)
    // console.log(ast)
    //  var obj = JSON.parse(list[1])
    routes.get('/', function(req,res){
        res.send(  final  )
    })
    }) 
   
 
module.exports = routes