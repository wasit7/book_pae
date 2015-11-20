# -*- coding: utf-8 -*-
"""
Created on Sat Nov 14 16:06:17 2015

@author: Methinee
"""

import pandas as pd
import numpy as np
from collections import defaultdict

df_file = pd.read_csv('../data/CS_table_No2_No4_new.csv',delimiter=";", skip_blank_lines = True, 
                 error_bad_lines=False)
                 
headers=list(df_file.columns.values)
subjects = {'courseId':[]}
students = {'0studentId':[]}
years = [52,53,54,55,56]
term = [1,2]
key_sub = defaultdict(list)
key_std = defaultdict(list)
key=[]

countSub = 0
countStd = 0
countEachSub = 0


#Create dictionary of list subjects
for sub in df_file[headers[4]]:
    if sub not in subjects['courseId']:
        subjects['courseId'].append(sub)
        countSub = countSub+1
#print subjects["courseId"]
#print "number of subjects are ",countSub
print "-----------------------------------------------"
#print key_sub
print "-----------------------------------------------"

#Create dictionary of list students
for std in df_file[headers[0]]:
    if std not in students['0studentId']:
        students['0studentId'].append(std)
        countStd = countStd+1

#print students['0studentId']
#print "number of students are ",countStd      
print "-----------------------------------------------"
subjects['courseId'].sort()

#Loop for giving all subject in dictionary len is num of students
for eachSub in subjects["courseId"]:
    #print eachSub
    countEachSub = countEachSub+1
    key_sub[countEachSub] = eachSub
#print key_sub

#Create column with all subjects
i = 1
for i in subjects["courseId"]:
    #print i
    students[i] = np.empty(len(students['0studentId']))
    students[i][:]=np.NAN

students['year'] = np.empty(len(students['0studentId']))
students['term'] = np.empty(len(students['0studentId']))
df_students = pd.DataFrame(students)


#Add grade into column subject
for record in df_file.values:
    student_grade = record[10]
print df_file[headers[10]]
#   for row in students['0studentId']:
#        for col in subjects["courseId"]:
#            if(df_file[headers[10]].notnull().values.any()):
#                print "Hellloooooooooo"
#                df_students.loc[students[col]]="%s"%student_grade
#                print "byeeeeee"
                
                   
                
            
            

        
             
writer = pd.ExcelWriter("table_No2_No4_new.xlsx")
pd.DataFrame(students).to_excel(writer,"grade")
writer.save()


