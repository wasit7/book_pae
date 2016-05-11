# -*- coding: utf-8 -*-
"""
Created on Wed Jan 20 11:04:32 2016

@author: BOOK
"""
import json
out={}
node=[]
edges=[]
with open("graph_reY.plain-ext") as f:
    content = f.readlines()
for n in content[1:]:
    line = n.split()
    
    if line[0] == "node":
        #print line[1:4]
        node.append({"COURSE_ID":line[1],"Y":line[2],"X":line[3]})
    elif line[0] == "edge":
       linepath = []
       for i in xrange(int(line[3])):
           x = line[4+(i*2)]
           y = line[5+(i*2)]
           mydict = {"x":x,"y":y}
           linepath.append(mydict)
       edges.append(linepath)           
out["node"]=node
out["edges"]=edges   
           
print out

with open("coordinate.json","w") as outfile:
    json.dump(out,outfile,sort_keys=True, indent=4, separators=(',',': '))