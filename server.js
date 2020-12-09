const express = require('express');
const cron = require('node-cron');
const sys = require('sys')
const exec = require('child_process').exec;
const app = express();
var path = require('path');
require('dotenv').config();
const port = process.env.PORT || 3000;
cron.schedule('* 12-20 * * *', function () {
    function puts(error, stdout, stderr) { sys.puts(stdout) }
    exec("python3 script.py", function (err, stdout, stderr) {
        console.log(stdout);
    })
}
);
cron.schedule('3 0-11,21-23 * * *', function () {
  function puts(error, stdout, stderr) { sys.puts(stdout) }
  exec("python3 script.py", function (err, stdout, stderr) {
      console.log(stdout);
  })
}
);
cron.schedule('1,31 * * * *', function () {
  console.log("Abin  31 minit log "); 
}
);
app.use(express.static(path.join(__dirname, 'public')));
app.use('/', require('./route/price'));


app.listen(port, (req, res) => {
  console.log(`server start on port ${port}`)
})
