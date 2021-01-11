#Make necessary import
import numpy as np
import pandas as pd
import itertools
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import PassiveAggressiveClassifier
from sklearn.metrics import accuracy_score, confusion_matrix


#Read the data
data_frame=pd.read_csv('data/news.csv')

#Get shape
data_frame.shape

#Get shape and head
print(data_frame.columns)