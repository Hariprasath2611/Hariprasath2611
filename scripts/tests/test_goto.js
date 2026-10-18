const puppeteer = require('puppeteer-core');
const path = require('path');

(async () => {
  const browser = await puppeteer.launch({
    executablePath: 'C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe',
    args: ['--no-sandbox', '--disable-setuid-sandbox']
  });
  const page = await browser.newPage();
  await page.setViewport({ width: 900, height: 500 });
  const url = 'file://' + path.resolve('assets/01-hero.svg').replace(/\\/g, '/');
  console.log('Navigating to:', url);
  await page.goto(url, { waitUntil: 'networkidle0' });
  await page.screenshot({ path: 'test_goto_hero.png' });
  await browser.close();
  console.log('Done');
})();
