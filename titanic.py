'''
=====
import libraries
'''
from __future__ import absolute_import, division, print_function
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import tensorflow as tf
from tensorflow import keras
from keras import layers
import seaborn as sns


'''
import data
'''
train_data = pd.read_csv('C:/Users/Hp-PC/Desktop/python/titanic/train_data.csv')
test_data = pd.read_csv('C:/Users/Hp-PC/Desktop/python/titanic/test_data.csv')

print(train_data.tail())

sns.pairplot(train_data[['Age','Survived', 'Sex', 'Title_4']], diag_kind = 'kde')
plt.show()