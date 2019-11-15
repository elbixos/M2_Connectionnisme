
from __future__ import absolute_import, division, print_function, unicode_literals

import pathlib
import tensorflow as tf
from tensorflow import keras
from tensorflow.keras import layers
import pandas as pd
import matplotlib.pyplot as plt

import os
import mymodel


dataset_path = keras.utils.get_file("evalMim.csv", "https://raw.githubusercontent.com/elbixos/M2_Connectionnisme/master/DeepMim/Sources/evalMim.csv")

column_names = ['line1','line2','line3','line4','eval']
raw_dataset = pd.read_csv(dataset_path, names=column_names,
                      na_values = "?", comment='\t',
                      sep=",", skipinitialspace=True)

dataset = raw_dataset.copy()
train_labels = dataset.pop('eval')


model2 = mymodel.build_model()
checkpoint_path = "training_1/cp.ckpt"
model2.load_weights(checkpoint_path)

def computeErrors(x,labels, predictions):
  truths = labels.values
  nbErrors=0
  for i in range(len(truths)) :
    if truths[i]*predictions[i][0] <=0 :
      nbErrors += 1
      print(i,"[",x.iloc[i,0],x.iloc[i,1],x.iloc[i,2],x.iloc[i,3],"]",truths[i],predictions[i][0])
  return nbErrors

pred = model2.predict(dataset)

print("Nb errors",computeErrors(dataset,train_labels,pred))
