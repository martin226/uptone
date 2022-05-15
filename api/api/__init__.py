__version__ = "0.1.0"

from api.predict import make_predictions
from flask import Flask, jsonify, request
from flask_cors import CORS

app = Flask(__name__)
CORS(app)


@app.route("/predict", methods=["POST"])
def predict():
    data = request.get_json()
    if not data or "tweets" not in data:
        return jsonify({"error": "No tweets provided"})
    tweets = data["tweets"]
    predictions = make_predictions(tweets)
    return jsonify({"predictions": predictions})
