const puppeteer = require('puppeteer-core');
const path = require('path');

(async () => {
  const browser = await puppeteer.launch({
    executablePath: 'C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe',
    args: ['--no-sandbox', '--disable-setuid-sandbox', '--font-render-hinting=none']
  });
  const page = await browser.newPage();
  await page.setViewport({ width: 900, height: 1530, deviceScaleFactor: 2 });
  const url = 'file://' + path.resolve('assets/profile-animated.svg').replace(/\\/g, '/');
  console.log('Rendering:', url);
  await page.goto(url, { waitUntil: 'networkidle0' });
  // wait 1s for fonts/animations
  await new Promise(r => setTimeout(r, 1000));
  await page.screenshot({ path: 'assets/profile-animated-render.png', fullPage: true });
  await browser.close();
  console.log('Saved assets/profile-animated-render.png');
})();
