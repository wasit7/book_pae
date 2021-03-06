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

for subject in subjects["courseId"]:
    print subject             
    df_sub = df_file[df_file['3COURSEID'] == subject]
    df_sub = df_sub.iloc[np.random.permutation(len(df_sub))]
    count_enrollment = df_sub['3COURSEID'].value_counts()
    #print "Number of %s enrollment: %s"%(subject,count_enrollment)

    A = df_sub.as_matrix()
    X = A[:,4:]
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
    
    sheet2.write(count, 0, subject)
    sheet2.write(count,1, scores.mean())
    book.save("RF_crossvalidation.xls")
    count = count+1
    
    print all subjects
    save trees to pickle file
    f = "tree/tree%s.pic"%subject
    with open(f, 'wb') as pickleFile:
        pickle.dump(clf, pickleFile, pickle.HIGHEST_PROTOCOL)

df_precision.plot(kind='bar')

#///////////////Find Importance Feature importances with forests of trees////////////////////
import matplotlib.pyplot as plt
from sklearn.datasets import make_classification

importances = forest.feature_importances_
std = np.std([tree.feature_importances_ for tree in forest.estimators_],
             axis=0)
indices = np.argsort(importances)[::-1]
list_grade = df_file.columns[4:]
# Print the feature ranking
print("Feature ranking:")

for f in range(X.shape[1]):
    print("%d. feature %s (%f)" % (f + 1, list_grade[indices[f]], importances[indices[f]]))


