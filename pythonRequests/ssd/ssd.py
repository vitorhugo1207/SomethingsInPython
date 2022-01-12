import json
import requests
import os

os.system("clear")

with open('config.json') as r:
  link = json.load(r)
  link = link['link']

response = requests.get(link)

print(response.text)
