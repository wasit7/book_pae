# -*- coding: utf-8 -*-
"""
Created on Fri Feb 19 22:12:25 2016

@author: Methinee
"""

import pandas as pd
import numpy as np
import pandas.io.sql as pd_sql
import sqlite3 as sql


df_file = pd.read_csv('../data/CS_table_No2_No4_new.csv',delimiter=";", skip_blank_lines = True, 
                 error_bad_lines=False,encoding='utf8')
                 
                 
df = {'sub_id':df_file['COURSEID'],'sub_name':df_file['COURSENAME'],
      'credit':df_file['CREDIT']}
      
df = pd.DataFrame(df)     
df_a = df.drop_duplicates('sub_id')
df_a = df_a[df_a['credit'] != 0]
 
writer = pd.ExcelWriter("create_uptodate.xlsx")
pd.DataFrame(df_a).to_excel(writer,"grade")
writer.save()            
        
                                 
con = sql.connect("D:/project/GitHub/book_pae/book/django/project/db.sqlite3")
#df = pd.DataFrame({'TestData': [1, 2, 3, 4, 5, 6, 7, 8, 9]}, dtype='float')
pd_sql.write_frame(df_a, name='mywebpage_subject',if_exists="append", con=con)
con.close()