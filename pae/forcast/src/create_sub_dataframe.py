# -*- coding: utf-8 -*-
"""
Created on Fri Feb 19 17:38:25 2016

@author: Administrator
"""

import pandas as pd
import pandas.io.sql as pd_sql
import sqlite3 as sql

df_file = pd.read_csv('../data/CS_table_No2_No4_new.csv',delimiter=";", skip_blank_lines = True, 
                 error_bad_lines=False,encoding='utf8')
                 
df = {'Sub_id':df_file['COURSEID'],'Sub_name':df_file['COURSENAME'],
      'credit':df_file['CREDIT']}
                 
df_a = pd.DataFrame(df)
                                 
con = sql.connect("subject.sqlite")
#df = pd.DataFrame({'TestData': [1, 2, 3, 4, 5, 6, 7, 8, 9]}, dtype='float')
pd_sql.write_frame(df_a, name='Subject',if_exists="append", con=con)
con.close()