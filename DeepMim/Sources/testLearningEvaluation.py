
from __future__ import absolute_import, division, print_function, unicode_literals

import pathlib
import tensorflow as tf
from tensorflow import keras
from tensorflow.keras import layers
import pandas as pd
import matplotlib.pyplot as plt

import os

def build_model():
  model = keras.Sequential([
    layers.Dense(32, activation='relu', input_shape=[4,]),
    layers.Dense(32, activation='relu'),
    layers.Dense(1)
  ])

  optimizer = tf.keras.optimizers.RMSprop(0.001)

  model.compile(loss='mse',
                optimizer=optimizer,
                metrics=['mae', 'mse'])
  return model

model = build_model()

dataset_path = keras.utils.get_file("evalMim.csv", "https://raw.githubusercontent.com/elbixos/M2_Connectionnisme/master/DeepMim/Sources/evalMim.csv")

column_names = ['line1','line2','line3','line4','eval']
raw_dataset = pd.read_csv(dataset_path, names=column_names,
                      na_values = "?", comment='\t',
                      sep=",", skipinitialspace=True)

dataset = raw_dataset.copy()
dataset.tail()

train_labels = dataset.pop('eval')
dataset.tail()
train_labels.tail()

example_batch = dataset[:5]
example_result = model.predict(example_batch)
example_result

checkpoint_path = "training_1/cp.ckpt"

model2 = build_model()

# Loads the weights
model2.load_weights(checkpoint_path)


example_batch = dataset[:5]
example_result = model2.predict(example_batch)
print(example_result)

examples_labels = train_labels[:5]
print(examples_labels)
