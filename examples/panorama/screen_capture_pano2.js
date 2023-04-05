const webdriver = require('selenium-webdriver');
const chrome = require('selenium-webdriver/chrome');
const fs = require('fs');

// Set up the Chrome driver
const options = new chrome.Options();
options.addArguments('--headless'); // run Chrome in headless mode
options.addArguments('--disable-gpu'); // disable hardware acceleration
const driver = new webdriver.Builder()
  .forBrowser('chrome')
  .setChromeOptions(options)
  .build();

// Navigate to the web page with the panorama element
driver.get('file:///Users/jwlee-pro/Library/CloudStorage/Dropbox/Workspace_2023/maps_naver_api/examples/panorama/1-panorama-simple.html');

// Wait for the panorama element to load
driver.wait(webdriver.until.elementLocated(webdriver.By.id('pano')));

// Get the dimensions of the panorama element
const pano = await driver.findElement(webdriver.By.id('pano'));
const dimensions = await pano.getSize();

// Take a screenshot of the panorama element
const screenshot = await driver.takeScreenshot();

// Crop the screenshot to the dimensions of the panorama element
const imageBuffer = Buffer.from(screenshot, 'base64');
const croppedBuffer = await sharp(imageBuffer)
  .extract({ left: 0, top: 0, width: dimensions.width, height: dimensions.height })
  .toBuffer();

// Save the cropped image to a file
fs.writeFileSync('panorama.png', croppedBuffer);

// Quit the driver
driver.quit();
