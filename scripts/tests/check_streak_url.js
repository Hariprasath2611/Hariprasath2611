const https = require('https');

const url = "https://github-readme-streak-stats.herokuapp.com/?user=HARIPRASATH2611&theme=tokyonight&border_radius=10";

https.get(url, (res) => {
    console.log(`URL: ${url}`);
    console.log(`StatusCode: ${res.statusCode}`);
    console.log(`Content-Type: ${res.headers['content-type']}`);
}).on('error', (e) => {
    console.error(`Error for ${url}: ${e.message}`);
});
