# -*- coding: utf-8 -*-
"""
Created on Thu Feb 25 23:15:03 2016

@author: Methinee
"""

import pandas as pd
import numpy as np
import pickle
import os 
import matplotlib
matplotlib.style.use('ggplot')
from collections import defaultdict


df_file = pd.read_excel('../src/transform.xlsx')
headers=list(df_file.columns.values)

#replace grade with integer and noplus in each grade
#{'':0, 'U#':1, 'U':1, 'S#':2, 'S':2, 'W':3, 'F':4, 'D':5, 'D+':5, 'C':6, 'C+':6, 'B':7, 'B+':7, 'A':8}
df_file = df_file.fillna(0)
df_file = df_file.replace(['A', 'B+', 'B', 'C+', 'C' , 'D+' , 'D' , 'F' , 'W' , 'S' , 'S#' , 'U' , 'U#'], 
                     [8, 7, 7, 6 , 6, 5, 5, 4, 3, 2, 2, 1, 1])
                     
#Select subject that have student enroll >=20 
count_courseId = df_file["3COURSEID"].value_counts() 
more20 = count_courseId[count_courseId[:]>=20]
df_more20 = df_file[df_file["3COURSEID"].isin(more20.index)]
df_more20.to_csv('../data'+'/df_more20.csv') #create new dataframe (>=20 enrollment)

#Create new file csv, all subject(>=20) and random order 
for m in more20.index:
    dfx=df_more20[df_more20["3COURSEID"].isin([m])]
    dfx=dfx.iloc[np.random.permutation(len(dfx))]
    dfx.to_csv('../data/df_sub_more20'+"/df_%s.csv"%m)

more20.plot(kind='bar')