const puppeteer = require('puppeteer');

(async () => {
  const browser = await puppeteer.launch();
  const page = await browser.newPage();
  await page.goto('file:///Users/jwlee-pro/Library/CloudStorage/Dropbox/Workspace_2023/maps_naver_api/examples/panorama/1-panorama-simple.html');
  
  // Wait for the panorama to load
  await page.waitForSelector('#pano');

  // Get the dimensions of the panorama
  const dimensions = await page.evaluate(() => {
    const pano = document.querySelector('#pano');
    return {
      width: pano.offsetWidth,
      height: pano.offsetHeight
    };
  });

  // Set the viewport to match the panorama dimensions
  await page.setViewport(dimensions);

  // Take a screenshot of the page
  await page.screenshot({ path: 'screenshot.png' });

  await browser.close();
})();
