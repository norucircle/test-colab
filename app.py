from flask import Flask, render_template, request

import tensorflow as tf
from tensorflow.keras import layers, Model
from tensorflow import keras
from tensorflow.keras.preprocessing import image
from tensorflow.keras.applications.imagenet_utils import preprocess_input
from tensorflow.keras.models import load_model
import os, sys

import pickle

from PIL import Image, ImageOps, ImageFile

import io
import requests
import numpy as np

app = Flask(__name__)

@app.route("/")
def index():
    return "Hello BOTNOI I'm BOTMAK!"

#function for [image link or image path --> image]
def getImage(imgpath):
    if imgpath.find('http')!=-1:
        r = requests.get(imgpath, allow_redirects=True, timeout=10)
        img = Image.open(io.BytesIO(r.content))
    else:
        img = Image.open(imgpath)
    return img.resize((224, 224))

# def extract_feature_resize(img_path):
#     img = getImage(img_path)
#     x = image.img_to_array(img)
#     img = None
#     x = np.expand_dims(x, axis=0)
#     x = preprocess_input(x)
    

@app.route("/predict")
def prediction():
    '''
    Test: 127.0.0.1:5000/predict?img_path=image_url
    '''
    img_path = request.args.get('img_path')

    h5_model = load_model('small_mobileNetV2_model.h5')
    img = getImage(img_path)
    x = image.img_to_array(img)
    img = 0
    x = np.expand_dims(x, axis=0)
    x = preprocess_input(x)
    pred = ( h5_model.predict(x) > 0.5 ).astype("int32") # 0.5 is thresold
    
    if pred:
        return "ไม่ได้เป็นโรคฝีดาษลิง"
    return "เป็นโรคฝีดาษลิง"

if __name__ == "__main__":
    app.run(debug=True)