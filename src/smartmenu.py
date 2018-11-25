from flask import Flask, render_template, request

from flask_cors import CORS

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
    bagimage = request.args.get('image')
    if bagimage:
            try:
                bagimageformat, bagimagefile = bagimage.split(';base64,')
                bagimageext = bagimageformat.split('/')[-1]
                #bag.image = ContentFile(base64.b64decode(bagimagefile),
                 #                       name=(str(time.time()).split('.')[0] + '-' + userid + '.' + bagimageext))
                #filename = photos.save(base64.b64decode(bagimagefile))
                #rec = Photo(filename=filename, user=g.user.id)
                #rec.store()
                #flash("Photo saved.")

                #response = funciondefinitiva(base64.b64decode(bagimagefile).decode('utf-8'))
                #return render_template('result.html', params=response)
            except:
                print("Error: Couldn't retrieve the image and decode it.")

    response = funciondefinitiva(bag.image)
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
