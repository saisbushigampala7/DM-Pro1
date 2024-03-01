#https://medium.com/analytics-vidhya/implementing-k-nearest-neighbours-knn-without-using-scikit-learn-3905b4decc3c

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

def predict(k, X_test):
   final_output = []
   for i in range(len(X_test)):
       dis_plus_i = []
       votes = []
       for j in range(len(X_train)):
           dist = distance(X_train[j], X_test[i])
           dis_plus_i.append([dist, j])
       dis_plus_i.sort()
       dis_plus_i = dis_plus_i[0:k]
       for dis_plus_i, j in dis_plus_i:
           votes.append(Y_train[j])
       ans = Counter(votes).most_common(1)[0][0]
       final_output.append(ans)
   return final_output


#prediction = predict(3, X_test)
print(X_train.iloc[0])

print("\nDone\n")
