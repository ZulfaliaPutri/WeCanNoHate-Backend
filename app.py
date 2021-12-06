import os

from flask import Flask, request
from keras.models import load_model
from joblib import load
from nltk.tokenize import TweetTokenizer
from flask_cors import CORS, cross_origin
import pandas as pd

app = Flask(__name__)


@app.route("/ping")
def ping():
    return "pong"


@app.route("/predict", methods=["POST"])
@cross_origin()
def trydo():
    input_payloads = request.json['inputs']
    if (not(input_payloads)):
        return "fail"

    predictions = model.predict(input_payloads)
    json_result = pd.Series(predictions).to_json(orient="values")
    return json_result


def tokenize(text):
    tokenizer = TweetTokenizer()
    return tokenizer.tokenize(text)


if __name__ == "__main__":
    model_path = open("./model/random_forest.joblib", "rb")
    model = load(model_path)

    print("running service")
    app.run(host="0.0.0.0", port="8080", debug=True)
