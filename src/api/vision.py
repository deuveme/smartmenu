import requests
import matplotlib.image
import base64

VISION_API_KEY = "AIzaSyAZtRpcJdd9mhTk_iMz4s5ss7O3lJwH9yM"

image = matplotlib.image.imread('../resources/menu1.jpg')


# Pass the image data to an encoding function.
def encode_image(image):
  image_content = image.read()
  return base64.b64encode(image_content)

IMAGE_ENCODED = encode_image(image); 




payload = {
  "requests": [
    {
      "image": {
        "content": "IMAGE_ENCODED"
          
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