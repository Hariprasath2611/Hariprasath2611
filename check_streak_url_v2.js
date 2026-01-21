const https = require('https');

const url = "https://github-readme-streak-stats.herokuapp.com/?user=HARIPRASATH2611&theme=tokyonight&border_radius=10";

console.log("Checking URL...");
https.get(url, (res) => {
    console.log(`StatusCode: ${res.statusCode}`);
    console.log(`Content-Type: ${res.headers['content-type']}`);

    let data = '';
    res.on('data', chunk => {
        // Just grab the first few bytes to see if it's valid
        if (data.length < 100) data += chunk;
    });

    res.on('end', () => {
        console.log(`Body Sample: ${data.substring(0, 100)}`);
    });

}).on('error', (e) => {
    console.error(`Error: ${e.message}`);
});
