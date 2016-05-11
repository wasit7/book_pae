# -*- coding: utf-8 -*-
"""
Created on Fri Apr 22 23:20:29 2016

@author: Methinee
"""
import pandas as pd
import json
from collections import defaultdict
countEachSubSort = 0
key_sub_sort = defaultdict(list)

subjects = []
countSub = 0
node = []
link= []
out={}
sources=[]
targets=[]

df_file = pd.read_excel('../data/transform_sort.xlsx')
headers=list(df_file.columns.values)

for sub in df_file[headers[3]]:
    if sub not in subjects: 
        subjects.append(sub)
        print "%s, index is %d"%(sub,subjects.index(sub))
        countSub = countSub+1
        node.append({"name":sub})
    
# Find index of source and target from book/graph1.gv  
df_st = pd.read_csv('../data/source-target.csv',delimiter=";", skip_blank_lines = True, 
                 error_bad_lines=False)
headers_st=list(df_st.columns.values)
df_st = df_st.dropna()

for source in df_st[headers_st[0]]:
    print "source is %s, index is %d"%(source,subjects.index(source))
    sources.append(subjects.index(source))
    
for target in df_st[headers_st[1]]:
    print "target is %s, index is %d"%(target,subjects.index(target))
    targets.append(subjects.index(target))
    
for i in xrange(0,70):
    link.append({"source":sources[i],"target":targets[i],"type": "licensing"})
    
out["node"]=node
out["link"]=link

#with open("subjects.json","w") as outfile:
#    json.dump(out,outfile,sort_keys=True, indent=4, separators=(',',': '))    