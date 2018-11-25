import requests
import matplotlib.image
import base64
#from maintraductor import idioma
from tragoo import translatelanguage

VISION_API_KEY = "AIzaSyAZtRpcJdd9mhTk_iMz4s5ss7O3lJwH9yM"

def encode_image(image):
  image_content = image.read()
  return base64.encodestring(image_content)


with open("resources/menu.jpg", "rb") as imageFile:
   str = base64.b64encode(imageFile.read())

payload = {
  "requests": [
    {
      "image": {
        "content": str.decode('utf-8')
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
    chars = set('$€')
    chars2 = set('0123456789')
    chars3 = set("',.")
    cond = palabra['palabra'][0] <= '9' and palabra['palabra'][0] >= '0' and palabra['palabra'][len(palabra['palabra'])-1] <= '9' and palabra['palabra'][len(palabra['palabra'])-1]
    if cond or any((c in chars) for c in palabra['palabra']) or (any((c in chars2) for c in palabra['palabra']) and any((c in chars3) for c in palabra['palabra'])):
        return True
    else:
        return False

def no_es_precio(palabra):
    return not es_precio(palabra)

def es_num(palabra):
    if palabra[len(palabra)-1] <= '9' and palabra[len(palabra)-1] >= '0':
        return True
    else:
        return False

response = requests.post('https://vision.googleapis.com/v1/images:annotate?key=' + VISION_API_KEY, json=payload).json()['responses'][0]['textAnnotations']

palabrasTotal = palabras_pos(response)

palabrasPrecios = list(filter(es_precio, palabrasTotal))

palabrasPlatos = list(filter(no_es_precio, palabrasTotal))

platos = []

for palabra in palabrasPrecios:
    ya_esta = False
    for plato in platos:
        if not ya_esta and palabra['y'] < plato['ymax'] and palabra['y'] > plato['ymin'] and palabra['x'] < plato['xmax'] and palabra['x'] > plato['xmin']:
            plato['precio'] += palabra['palabra'] + " "
            if palabra['x'] > plato['x']:
                plato['xmax'] = palabra['xmax'] + (palabra['xmax'] - palabra['xmin'])/2
                plato['xmin'] = palabra['xmin'] - (palabra['xmax'] - palabra['xmin'])/2
            ya_esta = True

    if not ya_esta:
        plato = {
            'ymax': palabra['ymax'] + (palabra['ymax'] - palabra['y']) / 2,
            'ymin': palabra['ymin'] - (palabra['ymax'] - palabra['y']) / 2,
            'xmax': palabra['xmax'] + (palabra['xmax'] - palabra['xmin'])/2,
            'xmin': palabra['xmin'] - (palabra['xmax'] - palabra['xmin'])/2,
            'y': palabra['y'],
            'x': palabra['x'],
            'precio': palabra['palabra'] + " ",
            'nombre': ""
        }
        platos.append(plato)

for palabra in palabrasPlatos:
    xmin = float("inf")
    platomin = {'nombre': ""}
    for plato in platos:
        if palabra['y'] < plato['ymax'] and palabra['y'] > plato['ymin'] and palabra['x'] < plato['x']:
            if plato['x'] < xmin:
                platomin = plato
                xmin = plato['x']
    platomin['nombre'] += palabra['palabra'] + " "

file = open("testfile.txt","w")
idioma = 'es'
for plato in platos:
    if plato['nombre'] != "" and plato['precio'] != "":
        file.write("Plato: " + translatelanguage(plato['nombre'],idioma) + "/ Precio: " + plato['precio'] + "\n")


file.close()