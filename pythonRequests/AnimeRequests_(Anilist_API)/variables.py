from Anilist_API_Study import *

def search_checker():
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
    return variables
