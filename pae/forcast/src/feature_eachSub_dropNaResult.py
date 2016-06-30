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
from sklearn.cross_validation import train_test_split
book = xlwt.Workbook(encoding="utf-8")
sheet1 = book.add_sheet("Precission Only Subject")



#----------------------Traning Data With Merging-----------------------
#df_file = pd.read_csv('../data/df_more20.csv',delimiter=",", skip_blank_lines = True, 
#                 error_bad_lines=False)
df_file = pd.read_csv('../data/df_dropSub_less20_dropNaResult.csv',delimiter=",", skip_blank_lines = True, 
                 error_bad_lines=False)
df_file = df_file.drop('Unnamed: 0',axis=1)
df_file = df_file.fillna(0)
df_file = df_file.replace(['A', 'B+', 'B', 'C+', 'C' , 'D+' , 'D' , 'F' , 'W' , 'S' , 'S#' , 'U' , 'U#'], 
                     [8, 7, 7, 6 , 6, 5, 5, 4, 3, 2, 2, 1, 1])
                 
count_courseId = df_file["3COURSEID"].value_counts() 
more20 = count_courseId

headers=list(df_file.columns.values)
subjects = []
countSub = 0
#Create dictionary of list subjects
for sub in df_file[headers[1]]:
    if sub not in subjects:
        subjects.append(sub)
        countSub = countSub+1
#Get subject that more 20 enrollment
count = 0
subjects.sort()
precision_rf={}
df_precision = more20.drop('CS231').copy()

list_allsub = df_file.columns[4:]
allSubject_df = pd.DataFrame(columns=[subjects],index=[list_allsub])
top10_df = pd.DataFrame(columns=[subjects])

subjects.remove('CS231')

for subject in subjects:
    #Create new Dataframe
    
    print subject             
    df_sub = df_file[df_file['3COURSEID'] == subject]
    df_sub = df_sub.iloc[np.random.permutation(len(df_sub))]
    count_enrollment = df_sub['3COURSEID'].value_counts()
    #print "Number of %s enrollment: %s"%(subject,count_enrollment)

    A = df_sub.as_matrix()
    X = A[:,6:116]
    X = X.astype(np.int64, copy=False)
    y = A[:,2]
    y = y.astype(np.int64, copy=False)

    # Split the data into a training set and a test set
    X_train, X_test, y_train, y_test = train_test_split(X, y,test_size=0.2,random_state=0)

    #Training data
    forest = RandomForestClassifier(n_estimators=10, max_depth=None, 
            min_samples_split=1, random_state=None, max_features=None)
    clf = forest.fit(X, y)
    scores = cross_val_score(clf, X, y, cv=5)
    print scores
    print "Random Forest Cross Validation of %s: %s"%(subject,scores.mean())
    precision_rf[subject] = scores.mean()
    df_precision.loc[subject]=precision_rf[subject]
    
    
    row_cm=[]
    Grade = ['A', 'B', 'C' , 'D' , 'F' , 'W' , 'S' , 'U' ,'na']
    row = []
    for cls in y_train:
        if cls not in row:
            row.append(cls)
    row.sort()
    #print row

   
    for i in xrange(len(row)):
        Grade = ['A', 'B', 'C' , 'D' , 'F' , 'W' , 'S' , 'U' ,'na']
        grade = Grade[::-1][row[i]]
        print grade
        row_cm.append(grade)
    print row_cm
    print len(row_cm)
    #print row_cm[1]    
    
    
    sheet1.write(count, 0, subject)
#    sheet1.write(count,3, scores.mean())
    sheet1.write(count,2,len(y_train))
#    sheet1.write(count,1, scores.mean()*100)
    sheet1.write(count,1,len(row_cm))
    book.save("RF_crossvalidation_dropNaResault.xls")
    count = count+1
    
    #print all subjects
    #save trees to pickle file
#    f = "tree_drop/tree%s.pic"%subject
#    with open(f, 'wb') as pickleFile:
#        pickle.dump(clf, pickleFile, pickle.HIGHEST_PROTOCOL)
        
    #///////////////Find Importance Feature importances with forests of trees///////////////////    
    importances = forest.feature_importances_
    std = np.std([tree.feature_importances_ for tree in forest.estimators_],
             axis=0)
    indices = np.argsort(importances)[::-1]
    list_grade = df_file.columns[6:117]
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

    

df_precision.plot(kind='bar')
df_precision.sort(ascending=False)
df_precision.plot(kind="bar")


writer = pd.ExcelWriter("feature_eachSub_dropNaResult.xlsx")
pd.DataFrame(allSubject_df).to_excel(writer,"all_feature")
pd.DataFrame(top10_df).to_excel(writer,"top10_feature")
writer.save()
