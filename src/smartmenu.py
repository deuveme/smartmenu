from flask import Flask, render_template, request

from flask_cors import CORS

from api.vision import hace_todo

from api.tragoo import translatelanguage

from locale import getdefaultlocale

app = Flask(__name__, template_folder='templates/')
CORS(app)


@app.route('/')
def render_static():
    return render_template('principal.html')



@app.route('/prueba')
def prueba():
    
    print("Entro en pruebas")
    response = []
    i = 1;
    for i in range(1,10):
        print (i)
        parcial = {}
        parcial["nombre"] = "Veerduras Fritas"
        parcial["precio"] = "12.50 CHF"
        response.append(parcial)
        
    print(response)           
    return render_template('result.html', params=response)

@app.route('/dataloggin', methods=['POST'])
def obtain():
    bagimage = request.form['image']
    idioma, _ = getdefaultlocale()
    idioma = idioma[0:2]
    print(bagimage)
    if bagimage:
        print("Image Received")
        try:
            print("Trying to decode")
            bagimageformat, bagimagefile = bagimage.split(';base64,')
            bagimageext = bagimageformat.split('/')[-1]
            parcial = bagimagefile
            response_without_translate = hace_todo(parcial)
            for plato in response_without_translate:
                if plato['nombre'] != "" and plato['precio'] != "":
                    plato['nombre'] = translatelanguage(plato['nombre'], idioma)
            return render_template('result.html', params=response_without_translate)
        except:
            print("Error: Couldn't retrieve the image and decode it.")

    print("No image recieved")
    return render_template('result.html')

@app.route('/result')
def search():
    # Get params
    #necessity = request.args.get('necessity')
    #location = request.args.get('location')
    #features = request.args.get('features')c
    #features = features.split('_')
    #del features[-1]

    # Sort places
    #response = sort_places(location, necessity, features)
    #return render_template('result.html', params=response)
    return render_template('result.html')


app.run(host="0.0.0.0", port=9090)
