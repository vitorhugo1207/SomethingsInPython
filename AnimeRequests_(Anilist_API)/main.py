import requests
import json
from query import *
# from variables import *

url = "https://graphql.anilist.co"
variables = ''

def get_information(url):
    if search.isnumeric():
        variables = {
            'id': search,
            'page': 1,
            'perPage': 1,
            'MediaType': "ANIME"
        }
    else:
        variables = {
            'search': search,
            'page': 1,
            'perPage': 1,
            'MediaType': "ANIME"
        }
    response = requests.post(url, json={"query": query, "variables": variables})
    return response

def main():
    response = get_information(url)
    response = response.json()
    print(response['data'])


search = "Fate/Zero"

if __name__ == '__main__':
    main()
