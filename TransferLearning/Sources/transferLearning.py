from __future__ import absolute_import, division, print_function, unicode_literals

import os

print ("importing numpy")
import numpy as np

import matplotlib.pyplot as plt

print ("importing tensorFlow")
import tensorflow as tf

keras = tf.keras

print ("importing tensorFlow datasets")
import tensorflow_datasets as tfds
tfds.disable_progress_bar()

print ("fin des imports")

SPLIT_WEIGHTS = (8, 1, 1)
splits = tfds.Split.TRAIN.subsplit(weighted=SPLIT_WEIGHTS)

print ("Loading DataBase Cats vs Dogs")
(raw_train, raw_validation, raw_test), metadata = tfds.load(
    'cats_vs_dogs', split=list(splits),
    with_info=True, as_supervised=True)

print ("Loading ok")

get_label_name = metadata.features['label'].int2str

for image, label in raw_train.take(2):
  plt.figure()
  plt.imshow(image)
  plt.title(get_label_name(label))


plt.show()

IMG_SIZE = 160 # All images will be resized to 160x160

def format_example(image, label):
  image = tf.cast(image, tf.float32)
  image = (image/127.5) - 1
  image = tf.image.resize(image, (IMG_SIZE, IMG_SIZE))
  return image, label

print ("formating the database")
train = raw_train.map(format_example)
validation = raw_validation.map(format_example)
test = raw_test.map(format_example)


BATCH_SIZE = 32
SHUFFLE_BUFFER_SIZE = 1000

print ("shuffling the database")
train_batches = train.shuffle(SHUFFLE_BUFFER_SIZE).batch(BATCH_SIZE)
validation_batches = validation.batch(BATCH_SIZE)
test_batches = test.batch(BATCH_SIZE)

IMG_SHAPE = (IMG_SIZE, IMG_SIZE, 3)

print ("get the base model")
# Create the base model from the pre-trained model MobileNet V2
base_model = tf.keras.applications.MobileNetV2(input_shape=IMG_SHAPE,
                                               include_top=False,
                                               weights='imagenet')
