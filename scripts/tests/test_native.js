const puppeteer = require('puppeteer-core');
const path = require('path');
const fs = require('fs');

const svg = `<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 900 200" width="100%" height="100%">
  <defs>
    <style>
      @keyframes pulse {
        0%, 100% { fill: #FF8A3D; }
        50% { fill: #B79CFF; }
      }
      .pulsing {
        animation: pulse 2s infinite;
      }
    </style>
  </defs>
  <rect width="900" height="200" fill="#1B1030" rx="24" />
  <rect x="40" y="40" width="200" height="120" rx="16" class="pulsing" />
  <text x="300" y="110" fill="#F6F1FF" font-family="sans-serif" font-size="28" font-weight="bold">Native SVG Working in IMG!</text>
</svg>`;

fs.writeFileSync('test_native.svg', svg);

(async () => {
  const browser = await puppeteer.launch({
    executablePath: 'C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe',
    args: ['--no-sandbox', '--disable-setuid-sandbox']
  });
  const page = await browser.newPage();
  await page.setViewport({ width: 900, height: 200 });
  const svgUrl = 'file://' + path.resolve('test_native.svg').replace(/\\/g, '/');
  await page.setContent(`<img src="${svgUrl}" width="900" />`);
  await page.screenshot({ path: 'test_native_render.png' });
  await browser.close();
  console.log('Done testing native SVG');
})();
