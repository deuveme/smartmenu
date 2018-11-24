import requests


VISION_API_KEY = "AIzaSyAZtRpcJdd9mhTk_iMz4s5ss7O3lJwH9yM"

payload = {
  "requests": [
    {
      "image": {
        "source": {
          "imageUri": "http://cafecomercialmadrid.com/wp-content/uploads/2017/04/menu-restaurant-cafe-comercial.jpg"
        }
      },
      "features": [
        {
          "type": "TEXT_DETECTION",
          "maxResults": 1
        }
      ]
    }
  ]
}

payload2 = {
  "polla":[
    {
      "image":{
        "content":"/9j/7QBEUGhvdG9...image contents...eYxxxzj/Coa6Bax//Z"
      },
      "features":[
        {
          "type":"LABEL_DETECTION",
          "maxResults":1
        }
      ]
    }
  ]
}



response = requests.post('https://vision.googleapis.com/v1/images:annotate?key=' + VISION_API_KEY, json=payload).json()

print(response)

print(3)