const puppeteer = require('puppeteer-core');
const path = require('path');
const fs = require('fs');

const svg = `<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 900 200" width="100%" height="100%">
  <foreignObject width="100%" height="100%">
    <div xmlns="http://www.w3.org/1999/xhtml" style="background: #1B1030; color: #F6F1FF; font-family: sans-serif; padding: 20px;">
      <h1 style="color: #FF8A3D;">Test ForeignObject</h1>
    </div>
  </foreignObject>
</svg>`;

fs.writeFileSync('test_fo.svg', svg);

(async () => {
  const browser = await puppeteer.launch({
    executablePath: 'C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe',
    args: ['--no-sandbox', '--disable-setuid-sandbox']
  });
  const page = await browser.newPage();
  await page.setViewport({ width: 900, height: 200 });
  const svgUrl = 'file://' + path.resolve('test_fo.svg').replace(/\\/g, '/');
  await page.setContent(`<img src="${svgUrl}" width="900" />`);
  await page.screenshot({ path: 'test_fo_render.png' });
  await browser.close();
  console.log('Done testing foreignObject');
})();
