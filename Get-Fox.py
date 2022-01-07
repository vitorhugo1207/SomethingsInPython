import requests
import json
import os

filePath = "~/fox/"
url = "https://randomfox.ca/floof/"

response = requests.get(url)
response = str(response.text)
response = json.loads(str(response))
response = response['image']

fileName = response[response.rfind("/")+1:]

os.system(f"wget {response} -P {filePath}")

os.system(f'feh --bg-fill --auto-zoom {filePath}{fileName}')
