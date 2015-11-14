# -*- coding: utf-8 -*-
"""
Created on Sat Nov 14 16:06:17 2015

@author: Methinee
"""

import pandas as pd
import numpy as np
from collections import defaultdict

df = pd.read_csv('../data/CS_table_No2_No4_new.csv',delimiter=";", skip_blank_lines = True, 
                 error_bad_lines=False)
                 
headers=list(df.columns.values)
subjects = {'courseId':[]}
students = {'0studentId':[]}
years = [52,53,54,55,56]
semester = [1,2]
key_sub = defaultdict(list)
key_std = defaultdict(list)
key=[]

countSub = 0
countStd = 0
countEachSub = 0


#Create dictionary of list subjects
for sub in df[headers[4]]:
    if sub not in subjects['courseId']:
        subjects['courseId'].append(sub)
        countSub = countSub+1
#print subjects["courseId"]
#print "number of subjects are ",countSub
print "-----------------------------------------------"
#print key_sub
print "-----------------------------------------------"

#Create dictionary of list students
for std in df[headers[0]]:
    if std not in students['0studentId']:
        students['0studentId'].append(std)
        countStd = countStd+1

#print students['studentId']
#print "number of students are ",countStd      
print "-----------------------------------------------"
subjects['courseId'].sort()

#Loop for giving all subject in dictionary len is num of students
for eachSub in subjects["courseId"]:
    #print eachSub
    countEachSub = countEachSub+1
    key_sub[countEachSub] = eachSub
print key_sub

Create column with all subjects
i = 1
for i in subjects["courseId"]:
    #print i
    students[i] = np.zeros(len(students['0studentId']))

##Create coloumn of all subjects
#for record in df.values: 
#    for student_id in record[:1]:
#        students[i][students['0studentId'].index(record[0])]+=1
      
        
             
writer = pd.ExcelWriter("table_No2_No4_new.xlsx")
pd.DataFrame(students).to_excel(writer,"grade")
writer.save()


