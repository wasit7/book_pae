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
sheet1 = book.add_sheet("Precission Without Merge")
sheet2 = book.add_sheet("Precission With Merge")
    
    
#----------------------Traning Data Without Merging-----------------------
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
df_precision_without = more20.copy()
    
for subject in subjects["courseId"]:
    print subject             
    df_sub = df_file[df_file['3COURSEID'] == subject]
    df_sub = df_sub.iloc[np.random.permutation(len(df_sub))]
    count_enrollment = df_sub['3COURSEID'].value_counts()
    #print "Number of %s enrollment: %s"%(subject,count_enrollment)
    
    A = df_sub.as_matrix()
    X = A[:,6:]
    X = X.astype(np.int64, copy=False)
    y = A[:,5]
    y = y.astype(np.int64, copy=False)
    
    #Training data
    forest = RandomForestClassifier(n_estimators=10, max_depth=None, 
                min_samples_split=1, random_state=None, max_features=None)
    clf = forest.fit(X, y)
    with_scores = cross_val_score(clf, X, y, cv=5)
    print with_scores
    print "Random Forest Cross Validation of %s: %s"%(subject,with_scores.mean())
    precision_rf[subject] = with_scores.mean()
    df_precision_without.loc[subject]=precision_rf[subject]
    print "-----------------------------------"
        
    sheet1.write(count, 0, subject)
    sheet1.write(count,1, with_scores.mean())
    book.save("RF_crossvalidation.xls")
    count = count+1
        
    #print all subjects
    #save trees to pickle file
    f = "tree/tree%s.pic"%subject
    with open(f, 'wb') as pickleFile:
        pickle.dump(clf, pickleFile, pickle.HIGHEST_PROTOCOL)
    
#df_precision.plot(kind='bar')
    
    #///////////////Find Importance Feature importances with forests of trees////////////////////
import numpy as np
import matplotlib.pyplot as plt
from sklearn.datasets import make_classification
    
importances = forest.feature_importances_
std = np.std([tree.feature_importances_ for tree in forest.estimators_],
                 axis=0)
indices = np.argsort(importances)[::-1]
list_grade = df_file.columns[6:]
# Print the feature ranking
print("Feature ranking:")
    
for f in range(X.shape[1]):
    print("%d. feature %s (%f)" % (f + 1, list_grade[indices[f]], importances[indices[f]]))
    
# Plot the feature importances of the forest
#plt.figure()
#plt.title("Feature importances")
#plt.bar(range(X.shape[1]), importances[indices],
#       color="r", yerr=std[indices], align="center")
#plt.xticks(range(X.shape[1]), indices)
#plt.xlim([-1, X.shape[1]])
#plt.show()  
    


















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
for sub in df_file[headers[4]]:
    if sub not in subjects['courseId']:
        subjects['courseId'].append(sub)
        countSub = countSub+1
#Get subject that more 20 enrollment
count = 0
subjects["courseId"].sort()
precision_rf={}
df_precision_with = more20.copy()
    
for subject in subjects["courseId"]:
    print subject             
    df_sub = df_file[df_file['3COURSEID'] == subject]
    df_sub = df_sub.iloc[np.random.permutation(len(df_sub))]
    count_enrollment = df_sub['3COURSEID'].value_counts()
    #print "Number of %s enrollment: %s"%(subject,count_enrollment)
    
    A = df_sub.as_matrix()
    X = A[:,6:]
    X = X.astype(np.int64, copy=False)
    y = A[:,5]
    y = y.astype(np.int64, copy=False)
    
    #Training data
    forest = RandomForestClassifier(n_estimators=10, max_depth=None, 
                min_samples_split=1, random_state=None, max_features=None)
    clf = forest.fit(X, y)
    without_scores = cross_val_score(clf, X, y, cv=5)
    print without_scores
    print "Random Forest Cross Validation of %s: %s"%(subject,without_scores.mean())
    precision_rf[subject] = without_scores.mean()
    df_precision_with.loc[subject]=precision_rf[subject]
    print "-----------------------------------"
        
    sheet1.write(count,3, subject)
    sheet1.write(count,4, without_scores.mean())
    book.save("RF_crossvalidation.xls")
    count = count+1
        
    #print all subjects
    #save trees to pickle file
    f = "tree/tree%s.pic"%subject
    with open(f, 'wb') as pickleFile:
        pickle.dump(clf, pickleFile, pickle.HIGHEST_PROTOCOL)
    
#df_precision.plot(kind='bar')
    
    #///////////////Find Importance Feature importances with forests of trees////////////////////
import numpy as np
import matplotlib.pyplot as plt
from sklearn.datasets import make_classification
    
importances = forest.feature_importances_
std = np.std([tree.feature_importances_ for tree in forest.estimators_],
                 axis=0)
indices = np.argsort(importances)[::-1]
list_grade = df_file.columns[6:]
# Print the feature ranking
print("Feature ranking:")
    
for f in range(X.shape[1]):
    print("%d. feature %s (%f)" % (f + 1, list_grade[indices[f]], importances[indices[f]]))
    
# Plot the feature importances of the forest
#plt.figure()
#plt.title("Feature importances")
#plt.bar(range(X.shape[1]), importances[indices],
#       color="r", yerr=std[indices], align="center")
#plt.xticks(range(X.shape[1]), indices)
#plt.xlim([-1, X.shape[1]])
#plt.show()  
    
    
    
    
    
    
    
#///////////////// Compare ///////////////////////////////////
DF = more20.copy()
compare = {}
for subject in subjects["courseId"]:
    DF1 = df_precision_with[subject]
    DF2 = df_precision_without[subject]
    compare[subject] = DF1-DF2
    print subject
    DF.loc[subject] = compare[subject]
DF.plot(kind='bar')

