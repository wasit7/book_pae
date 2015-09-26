# -*- coding: utf-8 -*-
"""
Created on Wed Sep 09 14:51:02 2015

@author: Methinee
"""

import pandas as pd
import numpy as np
from collections import defaultdict
from astropy.table import Table, Column

df = pd.read_csv('../data/CS_table_No2_No4_new.csv',delimiter=";", skip_blank_lines = True, 
                 error_bad_lines=False)
                 
headers=list(df.columns.values)
subjects = {'courseId':[]}
students = {'studentId':[]}
years = [52,53,54,55,56]
semester = [1,2]
key_sub = defaultdict(list)
key_std = defaultdict(list)
key=[]

countSub = 0
countStd = 0

#Create dictionary of list subjects
for sub in df[headers[4]]:
    if sub not in subjects['courseId']:
        subjects['courseId'].append(sub)
        countSub = countSub+1
        for keyCol in subjects['courseId']:
            key_sub[countSub] = keyCol         
print subjects["courseId"]
#print "number of subjects are ",countSub
#print "-----------------------------------------------"
print key_sub

#Create dictionary of list students
for std in df[headers[0]]:
    if std not in students['studentId']:
        students['studentId'].append(std)
        countStd = countStd+1
        for keyRow in students['studentId']:
            for y in years:    
                students['studentId'].append(y)
        
print students['studentId']       
#print "-----------------------------------------------"        
#print "number of students are ",countStd

#create table row are stdId+years+semester, column is key of subjects
#column = key_sub

#t = Table(column , names=(column))#
#t = Table(column , names=(subjects['courseId']))



        
    
"""table_No2_No4_out = pd.DataFrame(subjects) 
writer = pd.ExcelWriter("table_No2_No4_fomat.xlsx")
table_No2_No4_out.to_excel(writer,"grade")
writer.save()"""



