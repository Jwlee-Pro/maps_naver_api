import webbrowser
import os

# Replace latitude and longitude values in the HTML file
latitude = 37.3599605
longitude = 127.1059814

# Read the HTML file
with open('1-panorama-simple_revised.html', 'r') as f:
    html_content = f.read()

# Find the position argument in the JavaScript code
position_arg_start = html_content.find('position: new naver.maps.LatLng(')
position_arg_end = html_content.find('),', position_arg_start)
position_arg = html_content[position_arg_start+len('position: new naver.maps.LatLng('):position_arg_end]

# Replace the latitude and longitude values in the position argument
new_position_arg = f'{latitude}, {longitude}'
new_html_content = html_content[:position_arg_start+len('position: new naver.maps.LatLng(')] + new_position_arg + html_content[position_arg_end:]

# Write the modified HTML file
with open('1-panorama-simple_revised.html', 'w') as f:
    f.write(new_html_content)

# Open the modified HTML file in Chrome
chrome_path = '/Contents/MacOS/Google Chrome %s' # change the path to your Chrome executable
webbrowser.get(chrome_path).open('file://' + os.path.realpath('/Users/jwlee-pro/Library/CloudStorage/Dropbox/Workspace_2023/maps_naver_api/examples/panorama/custom_codes/1-panorama-simple_revised.html'))
