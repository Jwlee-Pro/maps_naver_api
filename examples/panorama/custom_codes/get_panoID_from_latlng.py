# %%

import requests

# Define the base URL of the Panorama API
base_url = "file:///Users/jwlee-pro/Library/CloudStorage/Dropbox/Workspace_2023/maps_naver_api/examples/panorama/custom_codes/1-panorama-simple_revised.html"

# Define your client ID
client_id = "5yl1yk9tal"

# Define your client secret
client_secret = "xxx"

# Define the latitude and longitude of the location you want to view
lat = 37.3599605
lng = 127.1058814

# Define the parameters for the Panorama API request
params = {
    "center": f"{lng},{lat}",
    "level": "3",
    "w": "800",
    "h": "600",
    "pan": "-135",
    "tilt": "29",
    "fov": "100"
}

# Add your client ID and client secret to the request headers
headers = {
    "X-NCP-APIGW-API-KEY-ID": client_id,
    "X-NCP-APIGW-API-KEY": client_secret
}

# Send a GET request to the Panorama API
response = requests.get(base_url, params=params, headers=headers)

# Check if the request was successful
if response.status_code == 200:
    # Get the panoID and POV from the response JSON
    panoID = response.json()["panoid"]
    pan = response.json()["pan"]
    tilt = response.json()["tilt"]
    fov = response.json()["fov"]

    print(f"PanoID: {panoID}")
    print(f"POV: ({pan}, {tilt}, {fov})")
else:
    # Print an error message if the request was not successful
    print(f"Error: {response.status_code}")

# %%
