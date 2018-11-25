import requests

VISION_API_KEY = "AIzaSyAZtRpcJdd9mhTk_iMz4s5ss7O3lJwH9yM"

def busca_img(query):
    payload = {
        "q": query,
        "num": 1,
        "start": 1,
        "imgSize": "small",
        "searchType": "image",
        "key": VISION_API_KEY,
        "cx": "001729826209899299709:luisubz3cc4"
    }

    response = requests.get('https://www.googleapis.com/customsearch/v1', params=payload).json()
    return response['items'][0]['link']
