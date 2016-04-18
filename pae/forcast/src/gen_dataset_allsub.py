# -*- coding: utf-8 -*-
"""
Created on Thu Feb 25 23:15:03 2016

@author: Methinee
"""

import pandas as pd
import numpy as np
import pickle
import os 
from collections import defaultdict


df_file = pd.read_excel('../data/transform_sort.xlsx')
headers=list(df_file.columns.values)

#replace grade with integer and noplus in each grade
#{'':0, 'U#':1, 'U':1, 'S#':2, 'S':2, 'W':3, 'F':4, 'D':5, 'D+':5, 'C':6, 'C+':6, 'B':7, 'B+':7, 'A':8}
df_file = df_file.fillna(0)
df_file = df_file.replace(['A', 'B+', 'B', 'C+', 'C' , 'D+' , 'D' , 'F' , 'W' , 'S' , 'S#' , 'U' , 'U#'], 
                     [8, 7, 7, 6 , 6, 5, 5, 4, 3, 2, 2, 1, 1])
                     

for i in xrange(5,208):
    #Create folder to keep datasets 
    newpath = r'D:\project\forcast\src\train%s' %(headers[i])
    if not os.path.exists(newpath):
        os.makedirs(newpath)
        
    #filter just cs213 in column #3
    cs = df_file.loc[df_file['3COURSEID'] == headers[i]]
    count = len(cs)

    #select row from 20%                      
    a = count/5
    a = int(a)
    a = a

    dataset = defaultdict(list)                     
    df_matrix = df_file.as_matrix()
    cs = df_matrix[df_matrix[:,3]==headers[i]]
    for j in range(0,5):
        if(count%5) == 0:        
            dataset_cs = cs[a*j:a*(j+1),:]
            dataset[j] = dataset_cs 
            
        else:
            if(count%5) == 1:
                dataset[0] = cs[a*j:a*(j+1)+1,:]
                dataset[1] = cs[a*j+1:a*(j+1)+1,:]
                dataset[2] = cs[a*j+1:a*(j+1)+1,:]
                dataset[3] = cs[a*j+1:a*(j+1)+1,:] 
                dataset[4] = cs[a*j+1:a*(j+1)+1,:]
            
            elif(count%5) == 2:
               dataset[0] = cs[a*j:a*(j+1)+1,:]
               dataset[1] = cs[a*j+1:a*(j+1)+2,:]
               dataset[2] = cs[a*j+2:a*(j+1)+2,:]
               dataset[3] = cs[a*j+2:a*(j+1)+2,:] 
               dataset[4] = cs[a*j+2:a*(j+1)+2,:]
            
            elif(count%5) == 3:
                dataset[0] = cs[a*j:a*(j+1)+1,:]
                dataset[1] = cs[a*j+1:a*(j+1)+2,:]
                dataset[2] = cs[a*j+2:a*(j+1)+3,:]
                dataset[3] = cs[a*j+3:a*(j+1)+3,:] 
                dataset[4] = cs[a*j+3:a*(j+1)+3,:]
            
            elif(count%5) == 4:
                dataset[0] = cs[a*j:a*(j+1)+1,:]
                dataset[1] = cs[a*j+1:a*(j+1)+2,:]
                dataset[2] = cs[a*j+2:a*(j+1)+3,:]
                dataset[3] = cs[a*j+3:a*(j+1)+4,:] 
                dataset[4] = cs[a*j+4:a*(j+1)+4,:]
            
        print "dataset0%d"%(j)
        print dataset[j]
        #print "dataset_213",dataset_213
                
        L = "L%02d"%(j)
        I = "I%02d"%(j)
        L = dataset[j][:,4]
        L = L.astype(np.int64, copy=False)
        I = dataset[j][:,5:]#L.shape
        I = I.astype(np.int64, copy=False)
        
        #save pickle file
        f = "train%s/dataset%02d.pic"%(headers[i],j)
        print f
        with open(f, 'wb') as pickleFile:
            theta_dim=1
            clmax = 14
            theta_range = I.shape[1]
            pickle.dump((clmax,theta_dim,theta_range,len(L),L,I,None), pickleFile, pickle.HIGHEST_PROTOCOL) 
    
        print "-------------------------------------------------------"

