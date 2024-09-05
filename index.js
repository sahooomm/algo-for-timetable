const http = require('http');
const fs = require('fs');
const childProcess = require('child_process');
const open = require('open');

const indexHtml = fs.readFileSync('index.html', 'utf8');
const timetableHtml = fs.readFileSync('timetable.html', 'utf8');

http.createServer((req, res) => {
  if (req.url === '/') {
    res.writeHead(200, {'Content-Type': 'text/html'});
    res.end(indexHtml);
  } else if (req.url === '/timetable') {
    res.writeHead(200, {'Content-Type': 'text/html'});
    res.end(timetableHtml);
  } else if (req.url === '/run_script' && req.method === 'POST') {
    childProcess.spawn('python', ['geneticAlgo.py']); // Replace 'script.py' with your script file name
    res.writeHead(302, {'Location': '/timetable'});
    res.end();
  } else {
    res.writeHead(404, {'Content-Type': 'text/plain'});
    res.end('Not Found');
  }
}).listen(3000, () => {
  console.log('Server listening on port 3000');
  open('http://localhost:3000'); // Open the index.html page in the default browser
});