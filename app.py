from flask import Flask, render_template, request

# import tensorflow as tf
# from tensorflow.keras import layers, Model
# from tensorflow import keras
# import os, sys

# from PIL import Image, ImageOps, ImageFile

app = Flask(__name__)

@app.route("/")
def index():
    return "Hello BOTNOI I'm BOTMAK!"

@app.route("/predict", methods=["POST"])
def prediction():
    return "Prediction"
    # sepal_length = float(request.form["sl"])
    # sepal_width = float(request.form["sw"])
    # petal_length = float(request.form["pl"])
    # petal_width = float(request.form["pw"])

    # prediction_class = iris_data_prediction(sepal_length, sepal_width, petal_length, petal_width)
    
    # return "<center><h1>ผลลัพธ์ของการพยากรณ์เป็นดอก {}</h1></center>".format(prediction_class)

if __name__ == "__main__":
    app.run(debug=True)