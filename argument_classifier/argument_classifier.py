import tensorflow as tf
import pandas as pd
from tensorflow import keras
import tensorflow_datasets as tfds
import numpy as np

TRAIN_DATA_URL = ''
TEST_DATA_URL = ''

train_file_path = tf.keras.utils.get_file('train-data.tsv',TRAIN_DATA_URL)
test_file_path = tf.keras.utils.get_file('valid-data.tsv',TEST_DATA_URL)


# model purpose : to predict whether someone's written text agrees or disagrees with an argument 

# function to predict messages based on model
# should return a list containing prediction and label, ex [.005, 'support']

def predict_argument(pred_text):
    return (prediction)

pred_text = 'I do not believe that is correct'

prediction = predict_argument(pred_text)
print(prediction)
