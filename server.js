
const express = require('express');
shell = require('shelljs');
const cron = require('node-cron')


require('dotenv').config();
const app = express();
const port = process.env.PORT || 3000;
app.use('/price',require('./route/price'));
app.use('/',require('./route/price'));




cron.schedule('0 30 * * * *', function() {
    console.log('---------------------');
    console.log('Running Cron Job');
    shell.exec('pm2 restart server.js price')
  
  });
  cron.schedule('0 0 0 1 * *', function() {
    console.log('---------------------');
    console.log('Log flushd');
    shell.exec('pm2 flush')
  
  });



app.listen(port,(req,res)=>{
    console.log(`server start on port ${port}`)
})