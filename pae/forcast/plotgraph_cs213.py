# -*- coding: utf-8 -*-
"""
Created on Thu Apr 14 18:21:40 2016

@author: Administrator
"""

import pandas as pd
import numpy as np
from sklearn.ensemble import RandomForestClassifier
from sklearn.cross_validation import cross_val_score
from matplotlib import pyplot as plt

#----------------------Traning Data-----------------------
df_file = pd.read_csv('data/df_more20.csv',delimiter=",", skip_blank_lines = True, 
                 error_bad_lines=False)
headers=list(df_file.columns.values)
subjects = {'courseId':[]}
countSub = 0
#Create dictionary of list subjects
for sub in df_file[headers[4]]:
    if sub not in subjects['courseId']:
        subjects['courseId'].append(sub)
        countSub = countSub+1
#Get subject that more 20 enrollment
count = 0
subjects["courseId"].sort()
          
df_sub = df_file[df_file['3COURSEID']=='TU154']
df_sub = df_sub.iloc[np.random.permutation(len(df_sub))]

A = df_sub.as_matrix()
X = A[:,6:]
X = X.astype(np.int64, copy=False)
y = A[:,5]
y = y.astype(np.int64, copy=False)

#Training data
clf_rf = RandomForestClassifier(n_estimators=10, max_depth=None, 
         min_samples_split=1, random_state=None, max_features=None)
scores = cross_val_score(clf_rf, X, y, cv=5)
clf = clf_rf.fit(X,y)
print scores
print "Random Forest Cross Validation: %s"%scores.mean()
print "-----------------------------------"

#i=0
#actual=np.array(y)
#predicted=np.zeros(len(y))
#n = 9
#cm = np.zeros((n,n))
#for i in xrange(len(y)):
#    predicted[i]=clf.predict(X)[i]
#    #print "actual grade:%d predicted grade:%d"%(actual[i],predict[i])  
#    cm[predicted[i],actual[i]] +=1 
#plt.hist(actual-predicted,50)
#print cm



    
