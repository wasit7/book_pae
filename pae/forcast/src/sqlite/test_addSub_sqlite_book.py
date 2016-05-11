# -*- coding: utf-8 -*-
"""
Created on Fri Feb 19 16:55:54 2016

@author: Administrator
"""

import pandas as pd
import pandas.io.sql as pd_sql
import sqlite3 as sql

df_file = pd.read_csv('../../data/CS_table_No2_No4_new.csv',delimiter=";", skip_blank_lines = True, 
                 error_bad_lines=False,encoding='utf8')
df_file = df_file.drop(['STUDENTID','ACADYEAR','CAMPUSID','SEMESTER','CURRIC','CAMPUSNAME','SECTIONGROUP','GRADE'],axis=1)

df_dropDup = df_file.drop_duplicates(['COURSEID'], take_last=True)
                 
                                
con = sql.connect("subject.sqlite")
#df = pd.DataFrame({'TestData': [1, 2, 3, 4, 5, 6, 7, 8, 9]}, dtype='float')
pd_sql.to_sql(df_dropDup, "all_subject", con, index=False)
con.close()