# -*- coding: utf-8 -*-
"""
Created on Thu Feb 25 23:15:03 2016

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
#filter just cs213 in column #3
cs213 = df_file.loc[df_file['3COURSEID'] == 'CS213']
count = len(cs213)

#test select row from 20%                      
a = 0.2*count
df_20 = cs213.iloc[:a-1]

#5 loops for make 5 dataset
dataset = np.zeros(5)
for i in range(0,5):
    df_213 = cs213.iloc[a*i:(a-1)+(a*i)]
    dataset[i] = i
    print "dataset0%d"%(dataset[i])
    print "df_213",df_213
    print "-------------------------------------------------------"

#add each dataset to pickle file
                   
# Randomly sample 70% of your dataframe
df_70 = df_file.sample(frac=0.2,random_state=None)

#  df rest from df_70
df_rest = df_file.loc[~df_file.index.isin(df_70.index)]
