import requests
import json
from query import *
# from variables import *

url = "https://graphql.anilist.co"


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
    test = json.loads(response.text)
    response = test["data"]["Page"]["media"]
    print(response)


search = "Fate/Zero"

if __name__ == '__main__':
    main()
