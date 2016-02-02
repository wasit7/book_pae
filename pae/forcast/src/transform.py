# -*- coding: utf-8 -*-
"""
Created on Tue Feb 02 15:59:05 2016

@author: Administrator
"""

import pandas as pd
import numpy as np
from collections import defaultdict

df_file = pd.read_csv('../data/CS_table_No2_No4_new.csv',delimiter=";", skip_blank_lines = True, 
                 error_bad_lines=False)

df = {'0STUDENTID':df_file['STUDENTID'],'1ACADYEAR':df_file['ACADYEAR'],
      '2SEMESTER':df_file['SEMESTER']}

headers=list(df_file.columns.values)
subjects = {'courseId':[]}
students = {'0studentId':[]}
countSub = 0
countStd = 0
countEachSub = 0
countEachStd = 0
key_sub = defaultdict(list)
key_std = defaultdict(list)

#Create dictionary of list subjects
for sub in df_file[headers[4]]:
    if sub not in subjects['courseId']:
        subjects['courseId'].append(sub)
        countSub = countSub+1

#Create dictionary of list students
for std in df_file[headers[0]]:
    if std not in students['0studentId']:
        students['0studentId'].append(std)
        countStd = countStd+1
        
#Loop for giving all subject in dictionary len is num of students
for eachSub in subjects["courseId"]:
    #print eachSub
    countEachSub = countEachSub+1
    key_sub[countEachSub] = eachSub
#print key_sub

#Create column with all subjects
i = 3
for i in subjects["courseId"]:
    #print i
    df[i] = np.empty(len(df['0STUDENTID']))
    df[i][:]=np.NAN


writer = pd.ExcelWriter("transform.xlsx")
pd.DataFrame(df).to_excel(writer,"grade")
writer.save()



