require('util')
const cron = require('node-cron');
const exec = require('child_process').exec;
cron.schedule('* 12-20 * * *', function () {
    function puts(error, stdout, stderr) { util.puts(stdout) }
    exec("python3 script.py", function (err, stdout, stderr) {
        console.log(stdout);
    })
}
);
cron.schedule('0,30 0-11,21-23 * * *', function () {
  function puts(error, stdout, stderr) { util.puts(stdout) }
  exec("python3 script.py", function (err, stdout, stderr) {
      console.log(stdout);
  })
}
);

// cron.schedule('* * * * * *', function () {
//     console.log("cron working")
// });

cron.schedule('15 */2 * * * ', function () {
    function puts(error, stdout, stderr) { util.puts(stdout) }
    exec("python script.py", function (err, stdout, stderr) {
        console.log(stdout);
        // console.log('data updating...')
    })
  }
  );