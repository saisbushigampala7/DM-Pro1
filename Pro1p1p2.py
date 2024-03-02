# Sai Bushigampala
# Data Mining Pro 1 - P1 and P2

import numpy as np 
import pandas as pd 
import matplotlib.pyplot as plt 
from math import sqrt
from collections import Counter

    
# reading file
training = r"C:\Users\ssbus\Downloads\Training dataset.xlsx"
train = pd.read_excel(training)
    
testing = r"C:\Users\ssbus\Downloads\Testing dataset.xlsx"
test = pd.read_excel(testing)

#Training Set--------------------------------------------------------------------

#Split Training Data - Part 1
X_train = train.iloc[:,2:]
Y_train = train.iloc[:,1]

X_test = test.iloc[:,2:]
Y_test = test.iloc[:,1]

#print(X.iloc[0].iloc[1]) - Row Value 0 column 1

#print(X.iloc[0,1]) - print value of row 0 column 1

Y_test_pred = []
k = 0

def pred(k, sort_keys):
    pos = 0
    neg = 0
    for i in range(0,k):
        if(Y_train[sort_keys[i]] == 1):
            pos += 1
        elif(Y_train[sort_keys[i]] == -1):
            neg += 1
    if(pos > neg):
        return 1
    elif(neg > pos):
        return -1
    
def KNN(k):
    for i in range(0, 19):
        p = 0
        q = 0
        r = 0
        jac_co = {}
        for j in range(0,180):
            for m in range(0,305):
                if(X_test.iloc[i, m] == 1 and X_train.iloc[j, m] == 1):
                    p += 1
                elif(X_test.iloc[i, m] == 0 and X_train.iloc[j, m] == 1):
                    q += 1
                elif(X_test.iloc[i, m] == 1 and X_train.iloc[j, m] == 0):
                    r +=1
            jac_co[j] = p/(p + q + r)        
        sort_list = dict(sorted(jac_co.items(), key=lambda x:x[1], reverse=True))
        sort_keys = list(sort_list.keys())
        Y_test_pred.append(pred(k, sort_keys))
    return Y_test_pred    

right = 0;
wrong = 0

k_fold = 13

Y_test_pred = KNN(k_fold)
for i in range(0, 19):
    if((Y_test_pred[i]) == (Y_test.iloc[i])):
        right = right + 1
    else:
        wrong = wrong + 1

print("\nKNN with k =", k_fold)
print("\n Incorrectly Predicted Wine: ", wrong)
print("\n Correctly Predicted Wine: ", right)
print("\n# of right Predictions/# of total predictions (in this case, only 19 predictions): Part 2 Calc:", right/19)

#