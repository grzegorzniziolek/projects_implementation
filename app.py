import pickle 
from flask import Flask, request, jsonify,app,url_for,render_template
import numpy as np
import pandas as pd

app = Flask(__name__)

regmodel = pickle.load(open('model.pkl', 'rb'))
scaler = pickle.load(open('scaler.pkl', 'rb'))

@app.route('/')
def home():
    return render_template('home.html')


@app.route("/predict", methods=['POST'])
def predict():
    data = request.json["data"]
    predict_request = np.array(list(data.values())).reshape(1, -1)
    predict_request = scaler.transform(predict_request)
    prediction = regmodel.predict(predict_request) 
    output = prediction[0]
    return jsonify(output)

@app.route("/predict_from_values", methods=['POST'])
def predict_from_values():
    data = [float(x) for x in request.form.values()]
    predict_request = np.array(data).reshape(1, -1)
    predict_request = scaler.transform(predict_request)
    prediction = regmodel.predict(predict_request)
    output = prediction[0]
    return render_template('home.html', prediction_text='Predicted House Price: ${:.2f}'.format(output))

if __name__ == "__main__":
    app.run(debug=True)

