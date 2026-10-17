const puppeteer = require('puppeteer-core');

(async () => {
  const browser = await puppeteer.launch({
    executablePath: 'C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe',
    args: ['--no-sandbox', '--disable-setuid-sandbox']
  });
  const page = await browser.newPage();
  await page.setViewport({ width: 900, height: 400, deviceScaleFactor: 2 });
  await page.setContent('<h1 style="color: #B79CFF; font-family: sans-serif;">Puppeteer Working!</h1>');
  await page.screenshot({ path: 'test_puppeteer.png' });
  await browser.close();
  console.log('Success!');
})();
