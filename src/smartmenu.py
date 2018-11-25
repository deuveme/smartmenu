from flask import Flask, render_template, request

from flask_cors import CORS

app = Flask(__name__, template_folder='templates/')
CORS(app)


@app.route('/')
def render_static():
    return render_template('principal.html')


app.run(host="0.0.0.0", port=9090)

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


