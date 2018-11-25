import requests
VISION_API_KEY = "AIzaSyAZtRpcJdd9mhTk_iMz4s5ss7O3lJwH9yM"
#NO ES NECESARIO LLAMARLA(ya que cuando traduces ya te detecta el idioma =)
def detectlanguage(texto):
    payload = {
        'q': texto,
        'key': VISION_API_KEY
    }
    response = requests.post('https://translation.googleapis.com/language/translate/v2/detect', params=payload).json()
    print (response)
texte = 'hello'
detectlanguage(texte)
idioma = 'en'

def translatelanguage(texte,idioma):
    payload = {
        'q': texte,
        'target': idioma,
        'key': VISION_API_KEY
    }
    response =requests.post('https://translation.googleapis.com/language/translate/v2', params=payload).json()
    return (response['data']['translations'][0]['translatedText'])

translatelanguage(texte,idioma)


