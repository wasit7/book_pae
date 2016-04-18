# -*- coding: utf-8 -*-
"""
Created on Thu Apr 07 14:09:20 2016

@author: Administrator
"""
import pandas as pd
import numpy as np
df_file = pd.read_csv('../data/df_m20/df_m20/df_CS341.csv',delimiter=",", skip_blank_lines = True, 
                 error_bad_lines=False)
                 

A = df_file.as_matrix()

L = A[:,3]
L = L.astype(np.int64, copy=False)
I = A[:,5:]#L.shape
I = I.astype(np.int64, copy=False)