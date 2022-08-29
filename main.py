import tensorflow as tf
from tensorflow.keras import layers, Model
from tensorflow import keras
import os, sys

from PIL import Image, ImageOps, ImageFile



def iris_data_prediction(sepal_length, sepal_width, petal_length, petal_width):
    iris = load_iris()
    inp = iris.data
    out = iris.target

    knn = KNeighborsClassifier(n_neighbors=5)

    knn.fit(inp, out)

    prediction = knn.predict([[sepal_length, sepal_width, petal_length, petal_width]])
    return iris['target_names'][prediction][0]

print(iris_data_prediction(2, 1, 3, 4))