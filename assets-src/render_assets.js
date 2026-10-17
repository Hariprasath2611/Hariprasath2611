const puppeteer = require('puppeteer-core');
const path = require('path');
const fs = require('fs');

const CHROME_PATH = 'C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe';

const blocks = [
  { name: '01-hero', file: '01-hero.html' },
  { name: '02-main-quest', file: '02-main-quest.html' },
  { name: '03-inventory', file: '03-inventory.html' },
  { name: '04-commit-log', file: '04-commit-log.html' },
  { name: '05-footer', file: '05-footer.html' }
];

(async () => {
  console.log('Launching Chrome from:', CHROME_PATH);
  const browser = await puppeteer.launch({
    executablePath: CHROME_PATH,
    args: ['--no-sandbox', '--disable-setuid-sandbox', '--force-color-profile=srgb']
  });

  for (const block of blocks) {
    const page = await browser.newPage();
    await page.setViewport({ width: 900, height: 100, deviceScaleFactor: 2 });
    
    const filePath = 'file://' + path.resolve(__dirname, 'assets', 'src', block.file).replace(/\\/g, '/');
    console.log(`Navigating to ${block.name}: ${filePath}`);
    
    await page.goto(filePath, { waitUntil: 'networkidle0' });
    await page.evaluateHandle('document.fonts.ready');
    
    // Give fonts an extra moment to settle
    await new Promise(r => setTimeout(r, 800));

    // Get body height
    const bodyHandle = await page.$('body');
    const boundingBox = await bodyHandle.boundingBox();

    const outPath = path.resolve(__dirname, 'assets', `${block.name}.png`);
    await bodyHandle.screenshot({
      path: outPath,
      omitBackground: false
    });
    
    console.log(`Saved ${outPath} (${Math.round(boundingBox.width * 2)}x${Math.round(boundingBox.height * 2)})`);
    await page.close();
  }

  await browser.close();
  console.log('All blocks successfully rendered!');
})();
