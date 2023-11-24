import tensorflow as tf 
import pandas as pd 
import numpy as np 
import matplotlib.pyplot as plt 
import keras 
from keras.models import Sequential 
from keras.layers import Dense 
from sklearn.metrics import confusion_matrix


data = pd.read_csv('heart_disease_uci.csv') 
print('Hello bangladesh')
print(data.head()) 

print('=====================')
print(data.describe())

print('====================')
print(data.isnull().any())


print('====================')
X = data.iloc[:,:13].values 
print(X)

# print('==================')
# y = data["target"].values 
# print(y)


