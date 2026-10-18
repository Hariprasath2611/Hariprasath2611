const https = require('https');

const options = {
    hostname: 'api.github.com',
    path: '/repos/Hariprasath2611/Hariprasath2611/actions/runs?per_page=5',
    headers: {
        'User-Agent': 'Node.js',
        // Using default public access. If this fails, we can't check without a token.
    }
};

https.get(options, (res) => {
    let data = '';
    res.on('data', chunk => { data += chunk; });
    res.on('end', () => {
        try {
            const runs = JSON.parse(data);
            if (runs.workflow_runs) {
                console.log(`Found ${runs.workflow_runs.length} runs.`);
                runs.workflow_runs.forEach(run => {
                    console.log(`Run ID: ${run.id}, Name: ${run.name}, Status: ${run.status}, Conclusion: ${run.conclusion}, Created: ${run.created_at}`);
                });
            } else {
                console.log("No runs found or API error: ", data.substring(0, 200));
            }
        } catch (e) {
            console.error(e.message);
        }
    });
}).on('error', (e) => {
    console.error(e);
});
