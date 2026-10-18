const https = require('https');

const options = {
    hostname: 'api.github.com',
    path: '/repos/Hariprasath2611/Hariprasath2611/actions/runs?per_page=1',
    headers: { 'User-Agent': 'Node.js' }
};

https.get(options, (res) => {
    let data = '';
    res.on('data', chunk => { data += chunk; });
    res.on('end', () => {
        try {
            const run = JSON.parse(data).workflow_runs[0];
            console.log(`Conclusion: ${run.conclusion}`);
        } catch (e) {
            console.error(e.message);
        }
    });
}).on('error', (e) => {
    console.error(e);
});
