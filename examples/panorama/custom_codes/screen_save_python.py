from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time
import base64
import io
from PIL import Image

# Set up the Chrome driver
chrome_options = Options()
chrome_options.add_argument('--headless') # run Chrome in headless mode
chrome_options.add_argument('--disable-gpu') # disable hardware acceleration
driver = webdriver.Chrome(options=chrome_options)

# Navigate to the web page with the panorama element
driver.get('file:///Users/jwlee-pro/Library/CloudStorage/Dropbox/Workspace_2023/maps_naver_api/examples/panorama/1-panorama-simple.html')

# Wait for the panorama element to load
time.sleep(1) # wait for the page to load, adjust as needed
pano = driver.find_element('id','pano')

# Get the dimensions of the panorama element
dimensions = pano.size

# Set the dimensions of the browser window to match the panorama element
driver.set_window_size(dimensions['width'], dimensions['height'])

# Take a screenshot of the entire browser window
screenshot_base64 = driver.get_screenshot_as_base64()
screenshot_bytes = base64.b64decode(screenshot_base64)

# Save the screenshot to a file
with open('panorama2.png', 'wb') as f:
    f.write(screenshot_bytes)

# Quit the driver
driver.quit()
