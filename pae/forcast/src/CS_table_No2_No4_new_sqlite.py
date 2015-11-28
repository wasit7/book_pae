# -*- coding: utf-8 -*-
"""
Created on Fri Nov 20 11:56:48 2015

@author: Administrator
"""


import pandas as pd
import pandas.io.sql as pd_sql
import sqlite3 as sql

df_file = pd.read_csv('../data/CS_table_No2_No4_new.csv',delimiter=";", skip_blank_lines = True, 
                 error_bad_lines=False,encoding='utf8')
                 
                 
                 
con = sql.connect("project.sqlite")
#df = pd.DataFrame({'TestData': [1, 2, 3, 4, 5, 6, 7, 8, 9]}, dtype='float')
pd_sql.to_sql(df_file, "registration", con)
con.close()