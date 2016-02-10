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
      '2SEMESTER':df_file['SEMESTER'],'3COURSEID':df_file['COURSEID'],'4RESULT':df_file['GRADE']}

headers=list(df_file.columns.values)
subjects = {'courseId':[]}
students = {'0studentId':[]}
countSub = 0
countStd = 0
countEachSub = 0
countEachSubSort = 0
countEachStd = 0
countEachYear = 0
countEachTerm = 0
key_sub_sort = defaultdict(list)
key_sub = defaultdict(list)
key_std = defaultdict(list)
key_year = defaultdict(list)
key_term = defaultdict(list)

#Create dictionary of list subjects
for sub in df_file[headers[4]]:
    if sub not in subjects['courseId']:
        subjects['courseId'].append(sub)
        countSub = countSub+1

#Create dictionary of list students(key of student)
for std in df_file[headers[0]]:
    if std not in students['0studentId']:
        students['0studentId'].append(std)
        countStd = countStd+1

#Create column with all subjects
i = 5
for i in subjects["courseId"]:
    #print i
    df[i] = np.empty(len(df['0STUDENTID']))
    df[i][:]=np.NAN

#key of student
for eachStd in df_file[headers[0]]:
    countEachStd = countEachStd+1
    key_std[countEachStd] = eachStd

#Key of year
for eachYear in df_file[headers[1]]:
    countEachYear = countEachYear+1
    key_year[countEachYear] = eachYear

#Key of month
for eachTerm in df_file[headers[2]]:
    countEachTerm = countEachTerm+1
    key_term[countEachTerm] = eachTerm

#Key of all subjects(1-)
for eachSub in df_file[headers[4]]:
    countEachSub = countEachSub+1
    key_sub[countEachSub] = eachSub


#Key of sorted subjects(1-203)
subjects['courseId'].sort()
for eachSubSort in subjects["courseId"]:
    countEachSubSort = countEachSubSort+1
    key_sub_sort[countEachSubSort] = eachSubSort
    
#Test loc 
df_a = pd.DataFrame(df)
#df_a.loc[0,'AN201'] = 0
#df_a.loc[1,'AN201'] = 'A'
#df_a.loc[1,key_sub_sort[2]] = 'B'
#df_a.loc[1,key_sub_sort[3]] = df_a.loc[1,'4RESULT']

#Test loop for access grade before
#count = 0
#for find in range(1,204):
#    if key_sub[2] == key_sub_sort[find]:
#        print "yeah"
#        df_a.loc[2,key_sub_sort[find]] = df_a.loc[1,'4RESULT']
#        break
#    else:
#        print "--"
#        count = count + 1
#print count

#Test Loop for add grade to subject column
#for i in range(0,46):
#    count = 0
#    for find in range(1,204):
#        if key_sub[i+1] == key_sub_sort[find]:
#            print "yeah"
#            df_a.loc[i+1,key_sub_sort[find]] = df_a.loc[i,'4RESULT']
#            break
#        else:
#            print "--"
#            count = count + 1
#    print count
    
#Test condition
#countmark = 0
#for i in range(0,15):
#    count = 0
#    if key_std[i+1] == key_std[i+2]:
#        if key_year[i+1] == key_year[i+2]:
#            if key_term[i+1] < key_term[i+2]:
#                for find in range(1,204):
#                    if key_sub[i+1] == key_sub_sort[find]:
#                        print "yeah"
#                        df_a.loc[i+1,key_sub_sort[find]] = df_a.loc[i,'4RESULT']
#                    else:
#                        print "--"
#                        count = count + 1
#                print count
#            else:
#                print "condition term"
#        else:
#            for find in range(1,204):
#                if key_sub[i+1] == key_sub_sort[find]:
#                    print "yeah"
#                    df_a.loc[i+1,key_sub_sort[find]] = df_a.loc[i,'4RESULT']
#                else:
#                    print "--"
#                    count = count + 1
#            print count
#           
#    else:
#        print "condition student"

#Add all before grade
start_record = 0
mark = 0 
change = 0
for i in range(0,31343):
    count = 0
    if key_std[i+1] == key_std[i+2]:
        if key_year[i+1] == key_year[i+2]:
            if key_term[i+1] < key_term[i+2]:
                for j in range(0,mark+1):
                    for find in range(1,204):
                        if key_sub[i+1-j] == key_sub_sort[find]:
                            print "yeah"
                            df_a.loc[i+1,key_sub_sort[find]] = df_a.loc[i-j,'4RESULT']
                        else:
                            print "--"
                            count = count + 1
                    print count
                change = 1
                
            elif key_term[i+1] == key_term[i+2]:
                print "condition term"
                if key_term[i+1] != key_term[start_record+1] or key_year[i+1] != key_year[start_record+1]:
                    for j in range(change,mark+1):
                        for find in range(1,204):
                            if key_sub[i+1-j] == key_sub_sort[find]:
                                print "yeah"
                                df_a.loc[i+1,key_sub_sort[find]] = df_a.loc[i-j,'4RESULT']
                            else:
                                print "--"
                                count = count + 1
                        print count
                    change = change+1
        else:
            for j in range(0,mark+1):
                for find in range(1,204):
                    if key_sub[i+1-j] == key_sub_sort[find]:
                        print "yeah"
                        df_a.loc[i+1,key_sub_sort[find]] = df_a.loc[i-j,'4RESULT']
                    else:
                        print "--"
                        count = count + 1
                print count
            change = 1
           
    else:
        print "condition student"
        start_record = i+1
        mark = -1
        change = 0
        
    mark = mark+1
print "change is",change
print "mark is",mark
print "i is",i
print "start is ",start_record         

writer = pd.ExcelWriter("transform.xlsx")
pd.DataFrame(df_a).to_excel(writer,"grade")
writer.save()



