
"""
Created on Wed Jan 20 11:04:32 2016

@author: BOOK
"""
import json
out={}
node={}
edges={}
with open("graph_reY.plain-ext") as f:
    content = f.readlines()
for n in content[1:]:
    line = n.split()

out["node"]=node
print out

#with open("c.json","w") as outfile:
    #json.dump(out,outfile,sort_keys=True, indent=4, separators=(',',': '))