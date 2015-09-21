# -*- coding: utf-8 -*-
"""
Created on Wed Sep 09 14:51:02 2015

@author: Administrator
"""

import pandas as pd
df = pd.read_csv('../data/CS_table_No2_No4.csv',delimiter=";", skip_blank_lines = True, 
                 error_bad_lines=False)

#print df
#print '------------------------------------------------------------------------'

headers=list(df.columns.values)
subjects={'courseId':[]}

for sub in df[headers[4]]:
    if sub not in subjects['courseId']:
        subjects['courseId'].append(sub)  
        
print subjects["courseId"]

