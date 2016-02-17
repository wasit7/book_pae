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
        node.append({"COURSE_ID":line[1],"X":line[2],"Y":line[3]})
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
           #co_x = {"x":x}
           #co_y = {"y":y}
           #print co_path
           #out.append({"head":line[1],"tail":line[2],"x":co_x,"y":co_y})
           #out.append({"x":x,"y":y})
           #out.append({"x":x ,"y":y})
        #count = line[3]  #count is number of control point
        #print line
        #for n in count:
        #out.append({"x":line[4],"y":line[5]})
            #out.append({"head":line[1],"tail":line[2],"x":line[4],"y":line[5]})
        #if line[3] == "4":
            #for n in line[4:12]:
                #intCo = [map(int, n) for n in line[4]]
                #intCo = float(line[4])
                #n = range(line[4],line[12],2)
            #n = line[4:12]
            #coordinate = [line]
            #out.append({"x"'{0}'.format(line)})
                
            #print 'x{0} y{1}'.format(line[0:2])
        #elif line[3] == "7":
           #l = line[4:18]
            #print l
        #elif line[3] == "10":
            #l = line[4:24]
            #print l
            #out.append({"count":line[3],"x":line[4:12]})
            #for n in line[4:12]:
                #out.append({"x":line[4],"y":line[5]})
            
        #if line[3] == "4":
            #out.append({"x":line[4],"y":line[5],"x":line[6],"y":line[7],
            #            "x":line[8],"y":line[9],"x":line[10],"y":line[11]})
        #elif line[3] == "7":
            #out.append({"x1":line[4],"y1":line[5],"x2":line[6],"y2":line[7],
            #            "x3":line[8],"y3":line[9],"x4":line[10],"y4":line[11],
            #            "x5":line[12],"y5":line[13],"x6":line[14],"y6":line[15],
            #            "x7":line[16],"y7":line[17]})
        #elif line[3] == "10":
            #out.append({"x1":line[4],"y1":line[5],"x2":line[6],"y2":line[7],
             #           "x3":line[8],"y3":line[9],"x4":line[10],"y4":line[11],
              #          "x5":line[12],"y5":line[13],"x6":line[14],"y6":line[15],
               #         "x7":line[16],"y7":line[17],"x8":line[18],"y8":line[19],
                #        "x9":line[20],"y9":line[21],"x10":line[22],"y10":line[23]})
print out

with open("coordinate.json","w") as outfile:
    json.dump(out,outfile,sort_keys=True, indent=4, separators=(',',': '))