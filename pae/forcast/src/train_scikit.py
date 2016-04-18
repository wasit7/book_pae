# -*- coding: utf-8 -*-
"""
Created on Wed Apr 13 16:02:16 2016

@author: Methinee
"""

import pandas as pd
import numpy as np
import pickle
import xlwt
from sklearn.ensemble import RandomForestClassifier
from sklearn.cross_validation import cross_val_score
book = xlwt.Workbook(encoding="utf-8")
sheet1 = book.add_sheet("Python Sheet 1")


#----------------------Traning Data-----------------------
df_file = pd.read_csv('../data/df_more20.csv',delimiter=",", skip_blank_lines = True, 
                 error_bad_lines=False)
                 
count_courseId = df_file["3COURSEID"].value_counts() 
more20 = count_courseId

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
precision_rf={}
df_precision = more20.copy()

for subject in subjects["courseId"]:
    print subject             
    df_sub = df_file[df_file['3COURSEID'] == subject]
    df_sub = df_sub.iloc[np.random.permutation(len(df_sub))]
    count_enrollment = df_sub['3COURSEID'].value_counts()
    print "Number of %s enrollment: %s"%(subject,count_enrollment)

    A = df_sub.as_matrix()
    X = A[:,6:]
    X = X.astype(np.int64, copy=False)
    y = A[:,5]
    y = y.astype(np.int64, copy=False)

    #Training data
    clf_rf = RandomForestClassifier(n_estimators=10, max_depth=None, 
            min_samples_split=1, random_state=None, max_features=None)
    clf = clf_rf.fit(X, y)
    scores = cross_val_score(clf, X, y, cv=5)
    print scores
    print "Random Forest Cross Validation of %s: %s"%(subject,scores.mean())
    precision_rf[subject] = scores.mean()
    df_precision.loc[subject]=precision_rf[subject]
    print "-----------------------------------"
    
    sheet1.write(count, 0, subject)
    sheet1.write(count,1, scores.mean())
    book.save("RF_crossvalidation.xls")
    count = count+1
    
    #save trees to pickle file
    f = "tree/tree%s.pic"%subject
    with open(f, 'wb') as pickleFile:
        pickle.dump(clf, pickleFile, pickle.HIGHEST_PROTOCOL)

df_precision.plot(kind='bar')
    