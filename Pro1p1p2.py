# Sai Bushigampala
# Data Mining Pro 1 - P1 and P2
# https://www.geeksforgeeks.org/ml-implementation-of-knn-classifier-using-sklearn/
#https://www.activestate.com/resources/quick-reads/how-to-access-a-column-in-a-dataframe-using-pandas/#:~:text=You%20can%20use%20the%20loc,Let's%20see%20how.&text=If%20we%20wanted%20to%20access,in%20order%20to%20retrieve%20it.


import numpy as np 
import pandas as pd 
from sklearn.model_selection import train_test_split 
from sklearn.neighbors import KNeighborsClassifier 
import matplotlib.pyplot as plt 

    
    # reading file
training = r"C:\Users\ssbus\Downloads\Training dataset.xlsx"
train = pd.read_excel(training)
    
testing = r"C:\Users\ssbus\Downloads\Testing dataset.xlsx"
test = pd.read_excel(testing)


X=train.iloc[:,2:]
    
y=train.iloc[:,1]

print(X)
    

    

