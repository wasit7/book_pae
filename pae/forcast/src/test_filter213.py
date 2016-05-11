# -*- coding: utf-8 -*-
"""
Created on Thu Feb 11 15:00:30 2016

@author: Methinee
"""


import pandas as pd
import numpy as np
import pickle

df_file = pd.read_excel('../src/transform.xlsx')
headers=list(df_file.columns.values)

df_file = df_file.fillna(0)
df_file = df_file.replace(['A', 'B+', 'B', 'C+', 'C' , 'D+' , 'D' , 'F' , 'W' , 'S' , 'S#' , 'U' , 'U#'], 
                     [13, 12, 11, 10 , 9, 8, 7, 6, 5, 4, 3, 2, 1])
                     
A = df_file.as_matrix()
temp = A[A[:,3]=='CS213']
L = temp[:,4]
L = L.astype(np.int64, copy=False)
I = temp[:,5:]#L.shape #I(X) is grade of all subject , L(Y) is grade of cs213
I = I.astype(np.int64, copy=False)

#S = df_file.as_matrix(columns=['4RESULT'])
#I = S[A[:,3]=='CS213']
#T = df_file.as_matrix(columns=['3COURSEID','4RESULT']

#with open('train/dataset00.pic', 'wb') as pickleFile:
#    #write label and feature vector
#    theta_dim=1
#    clmax = 14
#    theta_range = I.shape[1]
#    pickle.dump((clmax,theta_dim,theta_range,len(L),L,I,None), pickleFile, pickle.HIGHEST_PROTOCOL)
#    