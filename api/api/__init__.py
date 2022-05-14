__version__ = '0.1.0'

from flask import Flask, jsonify, request
app = Flask(__name__)

@app.route('/predict', methods=['POST'])
def predict():
    pass