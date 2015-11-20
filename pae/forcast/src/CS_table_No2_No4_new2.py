# -*- coding: utf-8 -*-
"""
Created on Sat Nov 14 16:06:17 2015

@author: Methinee
"""

import pandas as pd
import pandas.io.sql as pd_sql
import sqlite3 as sql

df_file = pd.read_csv('../data/CS_table_No2_No4_new.csv',delimiter=";", skip_blank_lines = True, 
                 error_bad_lines=False,encoding='utf8')
                 

df=pd.DataFrame({'STUDENTID':df_file.STUDENTID,
                 'ACADYEAR':df_file.ACADYEAR,
                 'SEMESTER':df_file.SEMESTER,
                 'COURSEID':df_file.COURSEID,
                 'GRADE':df_file.GRADE
                 })
column_order=['STUDENTID','ACADYEAR','SEMESTER','COURSEID','GRADE']
df = df[column_order] 
con = sql.connect("project.sqlite")
#df = pd.DataFrame({'TestData': [1, 2, 3, 4, 5, 6, 7, 8, 9]}, dtype='float')
pd_sql.to_sql(df, "registration", con)
con.close()