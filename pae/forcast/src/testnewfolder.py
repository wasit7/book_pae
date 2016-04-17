# -*- coding: utf-8 -*-
"""
Created on Tue Apr 05 01:14:21 2016

@author: Methinee
"""
import os 
import pandas as pd


df_file = pd.read_excel('../src/transform.xlsx')
headers=list(df_file.columns.values)

for i in xrange(5,208):
    newpath = r'D:\project\forcast\src\train%s' %(headers[i])
    if not os.path.exists(newpath):
        os.makedirs(newpath)