# -*- coding: utf-8 -*-
"""
Created on Wed May 25 00:18:25 2016

@author: Methinee
"""
import pandas as pd
import json
from collections import defaultdict
countEachSubSort = 0
key_sub_sort = defaultdict(list)

subjects = []
countSub = 0
link = []
out={}
sources=[]
targets=[]

df_file = pd.read_csv('../data/df_dropSub_less20.csv',delimiter=",", skip_blank_lines = True, 
                 error_bad_lines=False,encoding='utf8')
headers=list(df_file.columns.values)

for sub in df_file['3COURSEID']:
    if sub not in subjects: 
        subjects.append(sub)
#        print "%s, index is %d"%(sub,subjects.index(sub))
        countSub = countSub+1

subjects.sort()        

#///////For making Bachelor Graph (just subject has in Cirriculum)//////////////////
cs = 'CS'
tu = 'TU'
el = 'EL'
#print "\n".join(s for s in subjects if cs in s)

subjects_home = []
node = []
for s in subjects:
    if cs in s:
        print s
        subjects_home.append(s)
        node.append({"name":s})
    elif tu in s:
        print s
        subjects_home.append(s)
        node.append({"name":s})
    elif el in s:
        print s
        subjects_home.append(s)
        node.append({"name":s})

        
subjects_home.remove("CS105")
node.remove({"name":'CS105'})

subjects_home.remove("CS115")
node.remove({"name":'CS115'})

subjects_home.remove("CS211")
node.remove({"name":'CS211'})

subjects_home.remove("CS215")
node.remove({"name":'CS215'})

subjects_home.remove("CS231")
node.remove({"name":'CS231'})

subjects_home.remove("CS300")
node.remove({"name":'CS300'})


subjects_home.append('CS112')
node.append({"name":'CS112'})

subjects_home.append('CS327')
node.append({"name":'CS327'})

subjects_home.append('CS328')
node.append({"name":'CS328'})

subjects_home.append('CS357')
node.append({"name":'CS357'})

subjects_home.append('CS358')
node.append({"name":'CS358'})

subjects_home.append('CS359')
node.append({"name":'CS359'})

subjects_home.append('CS389')
node.append({"name":'CS389'})

subjects_home.append('CS406')
node.append({"name":'CS406'})

subjects_home.append('CS428')
node.append({"name":'CS428'})

subjects_home.append('CS439')
node.append({"name":'CS439'})

subjects_home.append('CS447')
node.append({"name":'CS447'})

subjects_home.append('CS448')
node.append({"name":'CS448'})

subjects_home.append('CS458')
node.append({"name":'CS458'})

subjects_home.append('CS469')
node.append({"name":'CS469'})

subjects_home.append('CS479')
node.append({"name":'CS479'})

subjects_home.append('CS496')
node.append({"name":'CS496'})

subjects_home.append('CS497')
node.append({"name":'CS497'})

subjects_home.append('CS499')
node.append({"name":'CS499'})

subjects_home.append('TH161')
node.append({"name":'TH161'})

subjects_home.append('PY228')
node.append({"name":'PY228'})

subjects_home.append('BA291')
node.append({"name":'BA291'})

subjects_home.append('EC210')
node.append({"name":'EC210'})

subjects_home.append('HO201')
node.append({"name":'HO201'})

subjects_home.append('MA211')
node.append({"name":'MA211'})

subjects_home.append('SC135')
node.append({"name":'SC135'})

subjects_home.append('SC185')
node.append({"name":'SC185'})

subjects_home.append('SC123')
node.append({"name":'SC123'})

subjects_home.append('SC173')
node.append({"name":'SC173'})

subjects_home.append('MA212')
node.append({"name":'MA212'})

subjects_home.append('MA332')
node.append({"name":'MA332'})

subjects_home.append('ST216')
node.append({"name":'ST216'})

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

with open("subjects_cc.json","w") as outfile:
    json.dump(out,outfile,sort_keys=True, indent=4, separators=(',',': '))
        