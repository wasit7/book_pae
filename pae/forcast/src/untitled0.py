# -*- coding: utf-8 -*-
"""
Created on Wed Apr 06 15:26:32 2016

@author: Administrator
"""

# -*- coding: utf-8 -*-
"""
Created on Thu Feb 25 23:15:03 2016

@author: Methinee
"""

import pandas as pd
import numpy as np
import pickle
from collections import defaultdict

df_file = pd.read_excel('../src/transform.xlsx')
headers=list(df_file.columns.values)

df_file = df_file.fillna(0)
df_file = df_file.replace(['A', 'B+', 'B', 'C+', 'C' , 'D+' , 'D' , 'F' , 'W' , 'S' , 'S#' , 'U' , 'U#'], 
                     [13, 12, 11, 10 , 9, 8, 7, 6, 5, 4, 3, 2, 1])
                     
#filter just cs213 in column #3
cs213 = df_file.loc[df_file['3COURSEID'] == 'CS222']
count = len(cs213)


#select row from 20%                      
a = 0.2*count
a = int(a)
a = a

dataset = defaultdict(list)                     
df_matrix = df_file.as_matrix()
cs213 = df_matrix[df_matrix[:,3]=='CS222']
for i in range(0,5):
    if(count%5) == 0:
        dataset_213 = cs213[a*i:a*(i+1),:]
        dataset[i] = dataset_213
        
    else:
        if(count%5) == 1:
            dataset[0] = cs213[a*i:a*(i+1)+1,:]
            dataset[1] = cs213[a*i+1:a*(i+1)+1,:]
            dataset[2] = cs213[a*i+1:a*(i+1)+1,:]
            dataset[3] = cs213[a*i+1:a*(i+1)+1,:] 
            dataset[4] = cs213[a*i+1:a*(i+1)+1,:]
            
        elif(count%5) == 2:
            dataset[0] = cs213[a*i:a*(i+1)+1,:]
            dataset[1] = cs213[a*i+1:a*(i+1)+2,:]
            dataset[2] = cs213[a*i+2:a*(i+1)+2,:]
            dataset[3] = cs213[a*i+2:a*(i+1)+2,:] 
            dataset[4] = cs213[a*i+2:a*(i+1)+2,:]
            
        elif(count%5) == 3:
            dataset[0] = cs213[a*i:a*(i+1)+1,:]
            dataset[1] = cs213[a*i+1:a*(i+1)+2,:]
            dataset[2] = cs213[a*i+2:a*(i+1)+3,:]
            dataset[3] = cs213[a*i+3:a*(i+1)+3,:] 
            dataset[4] = cs213[a*i+3:a*(i+1)+3,:]
            
        elif(count%5) == 4:
            dataset[0] = cs213[a*i:a*(i+1)+1,:]
            dataset[1] = cs213[a*i+1:a*(i+1)+2,:]
            dataset[2] = cs213[a*i+2:a*(i+1)+3,:]
            dataset[3] = cs213[a*i+3:a*(i+1)+4,:] 
            dataset[4] = cs213[a*i+4:a*(i+1)+4,:]
    print "dataset0%d"%(i)
    print dataset[i]
    
    #print "dataset_213",dataset_213
    L = "L%02d"%(i)
    I = "I%02d"%(i)
    L = dataset[i][:,4]
    L = L.astype(np.int64, copy=False)
    I = dataset[i][:,5:]#L.shape
    I = I.astype(np.int64, copy=False)

    #save pickle file
    f = "train/dataset%02d.pic"%(i)
    print f
    with open(f, 'wb') as pickleFile:
        theta_dim=1
        clmax = 14
        theta_range = I.shape[1]
        pickle.dump((clmax,theta_dim,theta_range,len(L),L,I,None), pickleFile, pickle.HIGHEST_PROTOCOL) 
    
    print "-------------------------------------------------------"

