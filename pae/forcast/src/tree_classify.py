# -*- coding: utf-8 -*-
"""
Created on Wed Apr 13 16:02:16 2016

@author: Methinee
"""

import pandas as pd
import numpy as np
import pickle
import xlwt
import matplotlib.pyplot as plt
from sklearn.datasets import make_classification
from sklearn.ensemble import RandomForestClassifier
from sklearn.cross_validation import cross_val_score
book = xlwt.Workbook(encoding="utf-8")
sheet1 = book.add_sheet("Precission Without Merge")
sheet2 = book.add_sheet("Precission With Merge")


#----------------------Traning Data With Merging-----------------------
#df_file = pd.read_csv('../data/df_more20.csv',delimiter=",", skip_blank_lines = True, 
#                 error_bad_lines=False)
df_file = pd.read_csv('../data/df_sub_more20_merge.csv',delimiter=",", skip_blank_lines = True, 
                 error_bad_lines=False)
                 
count_courseId = df_file["3COURSEID"].value_counts() 
more20 = count_courseId

headers=list(df_file.columns.values)
subjects = {'courseId':[]}
countSub = 0
#Create dictionary of list subjects
for sub in df_file[headers[1]]:
    if sub not in subjects['courseId']:
        subjects['courseId'].append(sub)
        countSub = countSub+1
#Get subject that more 20 enrollment
count = 0
subjects["courseId"].sort()
precision_rf={}
df_precision = more20.copy()

subject = 'CS213'
print subject             
df_sub = df_file[df_file['3COURSEID'] == subject]
df_sub = df_sub.iloc[np.random.permutation(len(df_sub))]
count_enrollment = df_sub['3COURSEID'].value_counts()
#print "Number of %s enrollment: %s"%(subject,count_enrollment)

A = df_sub.as_matrix()
X = A[:,6:209]
X = X.astype(np.int64, copy=False)
y = A[:,2]
y = y.astype(np.int64, copy=False)

#Training data
forest = RandomForestClassifier(n_estimators=10, max_depth=None, 
        min_samples_split=1, random_state=None, max_features=None)
clf = forest.fit(X, y)
scores = cross_val_score(clf, X, y, cv=5)
print scores
print "Random Forest Cross Validation of %s: %s"%(subject,scores.mean())
precision_rf[subject] = scores.mean()
df_precision.loc[subject]=precision_rf[subject]
print "-----------------------------------"

#print all subjects
#save trees to pickle file
f = "tree/tree%s.pic"%subject
with open(f, 'wb') as pickleFile:
    pickle.dump(clf, pickleFile, pickle.HIGHEST_PROTOCOL)

#///////////////////Classify with pickle without retrain(Model persistence)    
with open('tree/treeCS213.pic', 'rb') as pickleFile:
    clf2 = pickle.load(pickleFile)
    
df_labelX = pd.read_csv('../data/test_labelX.csv',delimiter=",", skip_blank_lines = True, 
                 error_bad_lines=False)

B = df_labelX.as_matrix()
X = B[:,6:209] #get all subject without term,year,province,schGpa
clf2.predict(X)
Grade=['A', 'B', 'C' , 'D' , 'F' , 'W' , 'S' , 'U' ,'na']
grade_predicted = Grade[::-1][clf2.predict(X)]
print "prediction of %s:"%subject,grade_predicted

