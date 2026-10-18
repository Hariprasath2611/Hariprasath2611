const puppeteer = require('puppeteer-core');
const path = require('path');

(async () => {
  const browser = await puppeteer.launch({
    executablePath: 'C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe',
    args: ['--no-sandbox', '--disable-setuid-sandbox', '--font-render-hinting=none']
  });
  const page = await browser.newPage();
  await page.setViewport({ width: 900, height: 1530, deviceScaleFactor: 2 });
  const rootDir = path.resolve(__dirname, '..');
  const svgPath = path.join(rootDir, 'assets', 'profile-animated.svg');
  const outPath = path.join(rootDir, 'assets', 'profile-animated-render.png');
  const url = 'file://' + svgPath.replace(/\\/g, '/');
  console.log('Rendering:', url);
  await page.goto(url, { waitUntil: 'networkidle0' });
  // wait 1s for fonts/animations
  await new Promise(r => setTimeout(r, 1000));
  await page.screenshot({ path: outPath, fullPage: true });
  await browser.close();
  console.log('Saved:', outPath);
})();
