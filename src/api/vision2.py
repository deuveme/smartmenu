import requests


VISION_API_KEY = "AIzaSyAZtRpcJdd9mhTk_iMz4s5ss7O3lJwH9yM"

payload = {
  "requests": [
    {
      "image": {
        "source": {
          "imageUri": "https://www.promociel.fr/media/catalog/product/cache/2/image/650x/040ec09b1e35df139433887a97daa66f/M/e/Menus_de_restaurant_8.gif"
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

# te convierte la query de la api de vision en un vector de palabras con sus posiciones en la foto
def palabras_pos(response):
    result = []
    for i in range(1, len(response)):
        elem = {}
        elem['palabra'] = response[i]['description']
        elem['xmin'] = response[i]['boundingPoly']['vertices'][0]['x']
        elem['ymin'] = response[i]['boundingPoly']['vertices'][0]['y']
        elem['xmax'] = response[i]['boundingPoly']['vertices'][2]['x']
        elem['ymax'] = response[i]['boundingPoly']['vertices'][2]['y']
        elem['y'] = (elem['ymax'] + elem['ymin'])/2
        elem['x'] = (elem['xmax'] + elem['xmin'])/2
        result.append(elem)
    return result


def es_precio(palabra):
    if palabra[0] <= '9' and palabra[0] >= '0' or palabra[0] == '$' or palabra[0] == '€' or palabra[0:3] == "CZK":
        return True
    else:
        return False



response = requests.post('https://vision.googleapis.com/v1/images:annotate?key=' + VISION_API_KEY, json=payload).json()['responses'][0]['textAnnotations']

palabras = palabras_pos(response)

platos = []

for palabra in palabras:
    ya_esta = False

    for plato in platos:
        if not ya_esta and palabra['y'] < plato['ymax'] and palabra['y'] > plato['ymin']:#si la palabra esta en la misma altura que el plato
            if es_precio(palabra['palabra']):
                plato['precio'] += palabra['palabra'] + " "
            else:
                plato['nombre'] += palabra['palabra'] + " "
            ya_esta = True

    if not ya_esta:
        plato = {
            'ymax': palabra['ymax'] + (palabra['ymax'] - palabra['y'])/2,
            'ymin': palabra['ymin'] - (palabra['ymax'] - palabra['y'])/2,
        }
        if es_precio(palabra['palabra']):
            plato['precio'] = palabra['palabra'] + " "
            plato['nombre'] = ""
        else:
            plato['nombre'] = palabra['palabra'] + " "
            plato['precio'] = ""
        platos.append(plato)

file = open("testfile.txt","w")

for plato in platos:
    if plato['nombre'] != "" and plato['precio'] != "":
        file.write("Plato: " + plato['nombre'] + "/ Precio: " + plato['precio'] + "\n")


file.close()