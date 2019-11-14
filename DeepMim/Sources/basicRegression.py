
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
    layers.Dense(16, activation='relu', input_shape=[4,]),
    layers.Dense(16, activation='relu'),
    layers.Dense(1)
  ])

  optimizer = tf.keras.optimizers.RMSprop(0.001)

  model.compile(loss='mse',
                optimizer=optimizer,
                metrics=['mae', 'mse'])
  return model

model = build_model()

dataset_path = 'evalMim.csv'
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
checkpoint_dir = os.path.dirname(checkpoint_path)

# Create a callback that saves the model's weights
cp_callback = tf.keras.callbacks.ModelCheckpoint(filepath=checkpoint_path,
                                                 save_weights_only=True,
                                                 verbose=1)



# Display training progress by printing a single dot for each completed epoch
class PrintDot(keras.callbacks.Callback):
  def on_epoch_end(self, epoch, logs):
    if epoch % 100 == 0: print('')
    print('.', end='')

EPOCHS = 1000

history = model.fit(
  dataset, train_labels,
  epochs=EPOCHS, validation_split = 0.2, verbose=0,
  callbacks=[PrintDot(),cp_callback])


def plot_history(history):
  hist = pd.DataFrame(history.history)
  hist['epoch'] = history.epoch

  plt.figure()
  plt.xlabel('Epoch')
  plt.ylabel('Mean Abs Error [eval]')
  plt.plot(hist['epoch'], hist['mae'],
           label='Train Error')
  plt.plot(hist['epoch'], hist['val_mae'],
           label = 'Val Error')
  plt.ylim([0,5])
  plt.legend()

  plt.figure()
  plt.xlabel('Epoch')
  plt.ylabel('Mean Square Error [$eval^2$]')
  plt.plot(hist['epoch'], hist['mse'],
           label='Train Error')
  plt.plot(hist['epoch'], hist['val_mse'],
           label = 'Val Error')
  plt.ylim([0,20])
  plt.legend()
  plt.show()


plot_history(history)

## Voyons comment il se débrouille maintenant en prédiction
example_batch = dataset[:5]
example_result = model.predict(example_batch)
example_result

examples_labels = train_labels[:5]
examples_labels

### Chargement du réseau

# Create a basic model instance
model2 = build_model()

# Loads the weights
model2.load_weights(checkpoint_path)


example_batch = dataset[:5]
example_result = model2.predict(example_batch)
example_result

examples_labels = train_labels[:5]
examples_labels

import numpy as np

board=[7,5,3,1]
npboard = np.asarray([board])
model2.predict(npboard)
