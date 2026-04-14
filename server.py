from flask import Flask, request, jsonify, render_template
import util
app = Flask(__name__)

@app.route('/')
def home():
    return render_template("app.html")

@app.route('/get_location_names', methods = ['GET'])
def get_location_names():
    response = jsonify({
        'locations' : util.get_location_names()
    })
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response

@app.route('/predict_home_price', methods=['POST'])
def predict_home_price():
    try:
        total_sqft = float(request.form.get('total_sqft', 0))
        location = request.form.get('location', '')
        bhk = int(request.form.get('bhk', 0))
        bath = int(request.form.get('bath', 0))

        if not location:
            return jsonify({'error': 'Location is required'})

        price = util.get_estimated_price(location, total_sqft, bhk, bath)

        response = jsonify({'estimated_price': price})
        response.headers.add('Access-Control-Allow-Origin', '*')
        return response

    except Exception as e:
        print("ERROR:", e)
        return jsonify({'error': str(e)})

import os

if __name__ == '__main__':
    print("Starting Python Flask Server for Bangalore House Price Prediction...")
    util.load_saved_artifacts()
    port = int(os.environ.get("PORT", 10000))
    app.run(host="0.0.0.0", port=port)
