# -*- coding: utf-8 -*-
"""
Created on Wed Jun 01 21:37:20 2016

@author: Administrator
"""

import pandas as pd
import pandas.io.sql as pd_sql
import sqlite3 as sql

df_file_all = pd.read_csv('../data/CS_table_No2_No4_new.csv',delimiter=";", skip_blank_lines = True, 
                 error_bad_lines=False,encoding='utf8')
                 
df_file_less = pd.read_csv('../data/df_dropSub_less20.csv',delimiter=",", skip_blank_lines = True, 
                 error_bad_lines=False,encoding='utf8')
                 
df_file_all = df_file_all.drop(['STUDENTID','ACADYEAR','CAMPUSID','SEMESTER','CURRIC','CAMPUSNAME','SECTIONGROUP','GRADE'],axis=1)

subjects = []
names = []
countSub = 0
subjects = []
link = []
out={}
sources=[]
targets=[]


for sub in df_file_less['3COURSEID']:
    if sub not in subjects:
        subjects.append(sub)
        countSub = countSub+1
subjects.sort()


df_db = df_file_all[df_file_all["COURSEID"].isin(subjects)]
df_db = df_db.drop_duplicates(['COURSEID'], take_last=True)  
df_db = df_db.sort(['COURSEID']) 

#Create lis of names subject
for name in df_db['COURSENAME']:
    names.append(name)
    


subjects_home = []
node = []

cs = 'CS'
tu = 'TU'
el = 'EL'

for index in xrange(0,111):
    s = subjects[index]
    n = names[index]   
    if cs in s:
        subjects_home.append(s)
        node.append({"id":s,"name":n})
    elif tu in s:
        subjects_home.append(s)
        node.append({"id":s,"name":n})
    elif el in s:
        subjects_home.append(s)
        node.append({"id":s,"name":n})

subjects_home.remove("CS105")
node.pop(2)

subjects_home.remove("CS115")
node.pop(3)

subjects_home.remove("CS211")
node.pop(3)

subjects_home.remove("CS215")
node.pop(5)

subjects_home.remove("CS231")
node.pop(7)

subjects_home.remove("CS300")
node.pop(18)


subjects_home.append('CS112')
node.append({"id":'CS112',"name":'Introduction to Object-Oriented Programming'})

subjects_home.append('CS327')
node.append({"id":'CS327',"name":'Digital Logic Design'})

subjects_home.append('CS328')
node.append({"id":'CS328',"name":'Compiler Construction'})

subjects_home.append('CS357')
node.append({"id":'CS357',"name":'Electronic Business'})

subjects_home.append('CS358')
node.append({"id":'CS358',"name":'Computer Simulation and Forecasting Techniques in Business'})

subjects_home.append('CS359')
node.append({"id":'CS359',"name":'Document Indexing and Retrieval'})

subjects_home.append('CS389')
node.append({"id":'CS389',"name":'Software Architecture'})

subjects_home.append('CS406')
node.append({"id":'CS406',"name":'Selected Topics in Advance Sofware Engineering Technology'})

subjects_home.append('CS428')
node.append({"id":'CS428',"name":'Principles of Multiprocessors Programming'})

subjects_home.append('CS439')
node.append({"id":'CS439',"name":'Selected Topics in Programming Languages'})

subjects_home.append('CS447')
node.append({"id":'CS447',"name":'Operating Systems II'})

subjects_home.append('CS448')
node.append({"id":'CS448',"name":'Software systems for advanced distributed computing'})

subjects_home.append('CS458')
node.append({"id":'CS458',"name":'Information Systems for Entrepreneur Management'})

subjects_home.append('CS469')
node.append({"id":'CS469',"name":'Selected Topics in Artificial Intelligent Systems'})

subjects_home.append('CS479')
node.append({"id":'CS479',"name":'Selected Topics in Computer Interface and Multimedia'})

subjects_home.append('CS496')
node.append({"id":'CS496',"name":'Rendering II'})

subjects_home.append('CS497')
node.append({"id":'CS497',"name":'Real-time Graphics'})

subjects_home.append('CS499')
node.append({"id":'CS499',"name":'Selected Topics in Computer Graphics'})

subjects_home.append('TH161')
node.append({"id":'TH161',"name":'Thai Usage'})

subjects_home.append('PY228')
node.append({"id":'PY228',"name":'Psychology Of Interpersonal Relations'})

subjects_home.append('BA291')
node.append({"id":'BA291',"name":'Introduction Of Business'})

subjects_home.append('EC210')
node.append({"id":'EC210',"name":'Introductory Economics'})

subjects_home.append('HO201')
node.append({"id":'HO201',"name":'Principles Of Management'})

subjects_home.append('MA211')
node.append({"id":'MA211',"name":'Calculus 1'})

subjects_home.append('SC135')
node.append({"id":'SC135',"name":'General Physics'})

subjects_home.append('SC185')
node.append({"id":'SC185',"name":'General Physics Laboratory'})

subjects_home.append('SC123')
node.append({"id":'SC123',"name":'Fundamental Chemistry'})

subjects_home.append('SC173')
node.append({"id":'SC173',"name":'Fundamental Chemistry Laboratory'})

subjects_home.append('MA212')
node.append({"id":'MA212',"name":'Calculus 2'})

subjects_home.append('MA332')
node.append({"id":'MA332',"name":'Linear Algebra'})

subjects_home.append('ST216')
node.append({"id":'ST216',"name":'Statistics For Social Science Students 1'})

subjects_home.sort()
node.sort()

## Find index of source and target from book/graph1.gv  
df_st = pd.read_csv('../data/source-target_home.csv',delimiter=";", skip_blank_lines = True, 
                 error_bad_lines=False)
headers_st=list(df_st.columns.values)
df_st = df_st.dropna()

for source in df_st[headers_st[0]]:
    #print "source is %s, index is %d"%(source,subjects_db.index(source))
    sources.append(subjects_home.index(source))
    
for target in df_st[headers_st[1]]:
    #print "target is %s, index is %d"%(target,subjects_db.index(target))
    targets.append(subjects_home.index(target))
    
for i in xrange(0,82): #In Bachelor has 83 links
    link.append({"source":sources[i],"target":targets[i],"type": "licensing"})
    
out["node"]=node
out["link"]=link

#with open("subjects_name.json","w") as outfile:
#    json.dump(out,outfile,sort_keys=True, indent=4, separators=(',',': '))