const https = require('https');

const options = {
    hostname: 'api.github.com',
    path: '/repos/Hariprasath2611/Hariprasath2611/actions/runs?per_page=5',
    headers: {
        'User-Agent': 'Node.js',
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
                    console.log(`Run ID: ${run.id}`);
                    console.log(`Name: ${run.name}`);
                    console.log(`Review: ${run.display_title}`);
                    console.log(`Status: ${run.status}`);
                    console.log(`Conclusion: ${run.conclusion}`);
                    console.log(`Created At: ${run.created_at}`);
                    console.log('---');
                });
            } else {
                console.log("No runs found or API error.");
            }
        } catch (e) {
            console.error(e.message);
        }
    });
}).on('error', (e) => {
    console.error(e);
});
