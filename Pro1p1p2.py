# Sai Bushigampala
# Data Mining Pro 1 - P1 and P2
# https://www.geeksforgeeks.org/ml-implementation-of-knn-classifier-using-sklearn/
#https://www.activestate.com/resources/quick-reads/how-to-access-a-column-in-a-dataframe-using-pandas/#:~:text=You%20can%20use%20the%20loc,Let's%20see%20how.&text=If%20we%20wanted%20to%20access,in%20order%20to%20retrieve%20it.
#https://sparkbyexamples.com/pandas/how-to-split-pandas-dataframe/

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

#Training Set--------------------------------------------------------------------

#Split Training Data - Part 1
X=train.iloc[:,2:]
    
y=train.iloc[:,1]

#Splitting Training Data into training and testing data
X_train, X_test, Y_train, Y_test = train_test_split(X, y, train_size=0.8, test_size=0.2)

#KNN with k=5 (Using Training Data to train model)
neigh2 = KNeighborsClassifier(n_neighbors=5)
neigh2.fit(X_train, Y_train.values.ravel())
Y_train_pred = neigh2.predict(X_train)


#Counting Correct and Incorrect Predictions - iterating over 40 wines - Part 2
right = 0
wrong = 0

for i in range(0, 40):
    if((Y_train_pred[i]) == (Y_test.iloc[i])):
      right = right + 1
    else:
      wrong = wrong + 1

print("\n----------Training DataSet-----------")
print("\n Wrong Class Predictions for Traning Set: ", wrong)
print("\n Right Class Predictions for Training Set: ", right)
print("\n# of right Predictions/# of total predictions (in this case, only 40 predictions): Part 2 Calc:", right/40)

#Testing Set---------------------------------------------------------------------

#Split Testing Data - Part 1
X=test.iloc[:,2:]
    
y=test.iloc[:,1]

#KNN with k=5 (Using Training Data to train model)
neigh2 = KNeighborsClassifier(n_neighbors=5)
neigh2.fit(X, y)
Y_pred = neigh2.predict(X)


#Counting Correct and Incorrect Predictions - iterating over 40 wines - Part 2
right = 0
wrong = 0

for i in range(0, 19):
    if((Y_pred[i]) == (y.iloc[i])):
      right = right + 1
    else:
      wrong = wrong + 1

print("\n----------Testing DataSet-----------")
print("\n Wrong Class Predictions for Testing Set: ", wrong)
print("\n Right Class Predictions for Testing Set: ", right)
print("\n# of right Predictions/# of total predictions (in this case, only 19 predictions): Part 2 Calc:", right/19)
    

