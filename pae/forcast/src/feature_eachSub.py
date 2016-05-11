# -*- coding: utf-8 -*-
"""
Created on Tue May 10 17:19:14 2016

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
subjects = []
countSub = 0
#Create dictionary of list subjects
for sub in df_file[headers[4]]:
    if sub not in subjects:
        subjects.append(sub)
        countSub = countSub+1
#Get subject that more 20 enrollment
count = 0
subjects.sort()
precision_rf={}
df_precision = more20.copy()

list_allsub = df_file.columns[6:]
allSubject_df = pd.DataFrame(columns=[subjects],index=[list_allsub])
top10_df = pd.DataFrame(columns=[subjects])

for subject in subjects:
    #Create new Dataframe
    
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
    scores = cross_val_score(clf, X, y, cv=5)
    print scores
    print "Random Forest Cross Validation of %s: %s"%(subject,scores.mean())
    precision_rf[subject] = scores.mean()
    df_precision.loc[subject]=precision_rf[subject]
    
    sheet2.write(count, 0, subject)
    sheet2.write(count,1, scores.mean())
    book.save("RF_crossvalidation.xls")
    count = count+1
    
    #print all subjects
    #save trees to pickle file
    f = "tree/tree%s.pic"%subject
    with open(f, 'wb') as pickleFile:
        pickle.dump(clf, pickleFile, pickle.HIGHEST_PROTOCOL)
        
    #///////////////Find Importance Feature importances with forests of trees///////////////////    
    importances = forest.feature_importances_
    std = np.std([tree.feature_importances_ for tree in forest.estimators_],
             axis=0)
    indices = np.argsort(importances)[::-1]
    list_grade = df_file.columns[6:]
    # Print the feature ranking
    print("Feature ranking:")

    for f in range(X.shape[1]):
        print("%d. feature %s (%f)" % (f + 1, list_grade[indices[f]], importances[indices[f]]))
        allSubject_df.loc[list_grade[indices[f]],subject] = importances[indices[f]]
        
    top10 = list_grade[indices][:10]
    print str(top10)
    for i in range(1,11):
        top10_df.loc[i,subject] = str(top10[i-1])
    print "-----------------------------------"


writer = pd.ExcelWriter("feature_eachSub.xlsx")
pd.DataFrame(allSubject_df).to_excel(writer,"all_feature")
pd.DataFrame(top10_df).to_excel(writer,"top10_feature")
writer.save()

 for i in r:

