import requests
import matplotlib.image
import base64
#from maintraductor import idioma
#from tragoo import translatelanguage
import re

VISION_API_KEY = "AIzaSyAZtRpcJdd9mhTk_iMz4s5ss7O3lJwH9yM"

def encode_image(image):
  image_content = image.read()
  return base64.encodestring(image_content)


# te convierte la query de la api de vision en un vector de palabras con sus posiciones en la foto
def palabras_pos(response):
    result = []
    for i in range(1, len(response)):
        elem = {}
        elem['palabra'] = response[i]['description']
        elem['xmin'] = response[i]['boundingPoly']['vertices'][0]['x']
        if 'y' in response[i]['boundingPoly']['vertices'][0]:
            elem['ymin'] = response[i]['boundingPoly']['vertices'][0]['y']
        else:
            elem['ymin'] = 0
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
    cond = palabra['palabra'] == 'CZK' or palabra['palabra'][0] <= '9' and palabra['palabra'][0] >= '0' and palabra['palabra'][len(palabra['palabra'])-1] <= '9' and palabra['palabra'][len(palabra['palabra'])-1]
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


def obtener_precio_traducido(stringPrecio):
    if stringPrecio.find(',') != -1:
        stringPrecio = stringPrecio.replace(',', '.')
    numero = re.findall(r'-?\d+\.?\d*', stringPrecio)
    if len(numero) <= 0:
        return "error"
    numero = float(numero[0])
    if stringPrecio.find('$') != -1:
        numero = numero * 0.99756
    elif stringPrecio.find('CZK') != -1:
        numero = numero * 0.04360
    elif stringPrecio.find('£') != -1:
        numero = numero * 1.27819
    else:
        numero = numero * 1.13033
    return str(round(numero, 2)) + " CHF"

def obtener_precio(stringPrecio):
    if stringPrecio.find(',') != -1:
        stringPrecio = stringPrecio.replace(',', '.')
    numero = re.findall(r'-?\d+\.?\d*', stringPrecio)
    char = "€"
    if len(numero) <= 0:
        return "error"
    numero = float(numero[0])

    if stringPrecio.find('$') != -1:
        char = '$'

    elif stringPrecio.find('CZK') != -1:
        char = 'CZK'

    elif stringPrecio.find('CHF') != -1:
        char = 'CHF'

    elif stringPrecio.find('£') != -1:
        char = '£'
    return str(round(numero, 2)) + " " + char



def sort_platos(plato):
    return plato['x'] + plato['y']


#imgpath = "resources/yeah.jpg"
#with open(imgpath, "rb") as imageFile:
#   yeah = base64.b64encode(imageFile.read()).decode('utf-8')
#imgpath = yeah

def hace_todo(imgpath):


    payload = {
      "requests": [
        {
          "image": {
            "content": imgpath
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
                    plato['xmax'] = palabra['xmax'] + (palabra['xmax'] - palabra['xmin'])
                    plato['xmin'] = palabra['xmin'] - (palabra['xmax'] - palabra['xmin'])
                ya_esta = True

        if not ya_esta:
            plato = {
                'ymax': palabra['ymax'] + (palabra['ymax'] - palabra['y']) / 2,
                'ymin': palabra['ymin'] - (palabra['ymax'] - palabra['y']) / 2,
                'xmax': palabra['xmax'] + (palabra['xmax'] - palabra['xmin']),
                'xmin': palabra['xmin'] - (palabra['xmax'] - palabra['xmin']),
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

    platos = sorted(platos, key=sort_platos)
    platosFinal = []
    for plato in platos:
        if plato["nombre"] != "" and plato["precio"] != "":
            platoFinal = {}
            platoFinal['nombre'] = plato['nombre']
            platoFinal['precioTraducido'] = obtener_precio_traducido(plato['precio'])
            platoFinal['precio'] = obtener_precio(plato['precio'])
            if platoFinal['precio'] != "error":
                platosFinal.append(platoFinal)

    #for plato in platosFinal:
    #    if plato['nombre'] != "" and plato['precio'] != "":
    #        file.write("Plato: " + translatelanguage(plato['nombre'],idioma) + "/ Precio: " + plato['precio'] + "\n")

    #file.close()

    return platosFinal

#hace_todo(imgpath)