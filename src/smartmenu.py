from flask import Flask, render_template, request

from flask_cors import CORS

app = Flask(__name__, template_folder='templates/')
CORS(app)


@app.route('/')
def render_static():
    return render_template('principal.html')


app.run(host="0.0.0.0", port=9090)

@app.route('/prueba')
def prueba():
    response = [{nombre:"Verduras Fritas", precio:"12.50"},
                {nombre: "Quiche", precio: "20.55"},
                {nombre: "Ternera Frita", precio: "60.25"},
                {nombre: "Verdurs Fritas", precio:"13.00"},
                {nombre: "Fondue", precio: "50.50"},
                {nombre: "Agua", precio: "5.00"}]
                
    return render_template('result.html', params=response)

@app.route('/dataloggin', methods=['POST'])
def obtain():
    bagimage = request.args.get('image')
    if bagimage:
            try:
                bagimageformat, bagimagefile = bagimage.split(';base64,')
                bagimageext = bagimageformat.split('/')[-1]
                bag.image = ContentFile(base64.b64decode(bagimagefile),
                                        name=(str(time.time()).split('.')[0] + '-' + userid + '.' + bagimageext))
            except:
                print("Error: Couldn't retrieve the image and decode it.")

    response = funciondefinitiva(bag.image)
    return render_template('result.html', params=response)

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


