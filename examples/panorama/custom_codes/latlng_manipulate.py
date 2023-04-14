import webbrowser
import os

# Replace latitude and longitude values in the HTML file
latitude = 37.475477693952875
longitude = 126.96060340959593
pan = 0

# Read the HTML file
with open('1-panorama-simple_revised.html', 'r') as f:
    html_content = f.read()

# Find the position and pan arguments in the JavaScript code
position_arg_start = html_content.find('position: new naver.maps.LatLng(')
position_arg_end = html_content.find('),', position_arg_start)
position_arg = html_content[position_arg_start+len('position: new naver.maps.LatLng('):position_arg_end]

pan_arg_start = html_content.find('pan: ')
pan_arg_end = html_content.find(',', pan_arg_start)
pan_arg = html_content[pan_arg_start+len('pan: '):pan_arg_end]

# Replace the latitude, longitude, and pan values
new_position_arg = f'{latitude}, {longitude}'
new_pan_arg = str(pan)

new_html_content = html_content[:position_arg_start+len('position: new naver.maps.LatLng(')] + new_position_arg + html_content[position_arg_end:]
new_html_content = new_html_content[:pan_arg_start+len('pan: ')] + new_pan_arg + new_html_content[pan_arg_end:]

# Write the modified HTML file
with open('1-panorama-simple_revised.html', 'w') as f:
    f.write(new_html_content)

# Open the modified HTML file in Chrome
chrome_path = '/Contents/MacOS/Google Chrome %s' # change the path to your Chrome executable
webbrowser.get(chrome_path).open('file://' + os.path.realpath('/Users/jwlee-pro/Library/CloudStorage/Dropbox/Workspace_2023/maps_naver_api/examples/panorama/custom_codes/1-panorama-simple_revised.html'))
