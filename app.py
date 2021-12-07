import os

from flask import Flask, request
from keras.models import load_model
from joblib import load
from nltk.tokenize import TweetTokenizer
from flask_cors import CORS, cross_origin
import pandas as pd

app = Flask(__name__)
CORS(app)


@app.route("/ping")
def ping():
    return "pong"


@app.route("/predict", methods=["POST"])
@cross_origin()
def predict_function():
    input_payloads = request.json["inputs"]

    predictions = model.predict(input_payloads)
    json_result = pd.Series(predictions).to_json(orient="values")
    return json_result


###
# this function is required by the model as it needs the text to be tokenized first with the same tokenization algorithm
# before supplied to the machine learning model
def tokenize(text):
    tokenizer = TweetTokenizer()
    return tokenizer.tokenize(text)


if __name__ == "__main__":
    model_path = open("./model/random_forest.joblib", "rb")
    model = load(model_path)

    print("running service")
    app.run(host="0.0.0.0", port="8080", debug=True)
