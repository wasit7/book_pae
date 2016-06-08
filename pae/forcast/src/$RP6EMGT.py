# -*- coding: utf-8 -*-
"""
Created on Fri May 13 22:59:53 2016

@author: Methinee
"""
import pandas as pd
import numpy as np
import pickle

df_file = pd.read_csv('../data/df_sub_more20_merge.csv',delimiter=",", skip_blank_lines = True, 
                 error_bad_lines=False)
headers=list(df_file.columns.values)
subjects = []
countSub = 0
#Create dictionary of list subjects
for sub in df_file['3COURSEID']:
    if sub not in subjects:
        subjects.append(sub)
        countSub = countSub+1
# Function definition is here
def classify( X ):
    with open('tree/treeCS213.pic', 'rb') as pickleFile:
        clf2 = pickle.load(pickleFile)
    clf2.predict(X)
    Grade=['A', 'B', 'C' , 'D' , 'F' , 'W' , 'S' , 'U' ,'na']
    grade_predicted = Grade[::-1][clf2.predict(X)]
    print "prediction: ",grade_predicted 
   
    return

#Example1: Create lable X from Pae's Transcript.. result of CS213 should be "C"
#df_labelX = pd.read_csv('../data/test_labelX.csv',delimiter=",", skip_blank_lines = True, 
#                 error_bad_lines=False)
#B = df_labelX.as_matrix()
#X = B[:,6:209] #get all subject without term,year,province,schGpa


#Example2: Create lable X from first record of csv only cs213.. result of CS213 should be "C"

subject = 'CS213'
print subject             
df_sub = df_file[df_file['3COURSEID'] == subject]
df_sub = df_sub.iloc[np.random.permutation(len(df_sub))]

A = df_sub.as_matrix()
X = A[0,6:209]

classify( X );

