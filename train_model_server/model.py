import tensorflow as tf
from tensorflow import keras
import tensorflow.keras.backend as K
import numpy as np
import pickle
import os

def get_model():
    model = keras.Sequential([
        keras.layers.Flatten(input_shape=(28, 28)),
        keras.layers.Dense(128, activation=tf.nn.relu),
        keras.layers.Dense(10, activation=tf.nn.softmax)
    ])
    output_class = tf.argmax(model.output, axis=-1, name="output_class")

    model.compile(optimizer='adam',
                  loss='sparse_categorical_crossentropy',
                  metrics=['accuracy'])
    return model

def train_model(file_name):
    f = open("upload_files/train_data.pickle","rb")
    (train_x,train_y) = pickle.load(f)
    f.close()
    train_x = train_x/255.0
    print(train_x[0])
    os.remove("upload_files/train_data.pickle")
    model = get_model()
    model.fit(train_x, train_y, epochs=10)
    model.save("model/model.h5")

