const puppeteer = require('puppeteer-core');
const path = require('path');
const fs = require('fs');

(async () => {
  const browser = await puppeteer.launch({
    executablePath: 'C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe',
    args: ['--no-sandbox', '--disable-setuid-sandbox']
  });
  const page = await browser.newPage();
  await page.setViewport({ width: 900, height: 200 });
  
  const svg = `<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 900 200" width="100%" height="100%">
    <rect width="900" height="200" fill="#1B1030" />
    <text x="50" y="80" fill="#F6F1FF" font-family="'Syne', system-ui, sans-serif" font-size="48" font-weight="800">Hariprasath</text>
    <text x="50" y="130" fill="#CFC4EA" font-family="'DM Sans', system-ui, sans-serif" font-size="18">I build web and mobile apps end to end.</text>
  </svg>`;
  
  fs.writeFileSync('test_text.svg', svg);
  
  await page.goto('file://' + path.resolve('test_text.svg').replace(/\\/g, '/'));
  await page.screenshot({ path: 'test_text_render.png' });
  await browser.close();
  console.log('Text rendered successfully');
})();
