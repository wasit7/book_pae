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
cs213 = df_file.loc[df_file['3COURSEID'] == 'CS213']
count = len(cs213)

##test select row from 20%                      
a = 0.2*count
a = int(a)
a = a

dataset = defaultdict(list)                     
df_matrix = df_file.as_matrix()
cs213 = df_matrix[df_matrix[:,3]=='CS213']
for i in range(0,5):
    dataset_213 = cs213[a*i:a*(i+1),:]
    dataset[i] = dataset_213 
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

#dataset00 = cs213[0:a,:]
#dataset01 = cs213[a:a*2,:]
#dataset02 = cs213[a*2:a*3,:]
#dataset03 = cs213[a*3:a*4,:]
#dataset04 = cs213[a*4:a*5,:]
