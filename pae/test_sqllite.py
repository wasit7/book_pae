# -*- coding: utf-8 -*-
"""
Created on Fri Nov 20 12:05:39 2015

@author: Wasit
"""

import pandas as pd
import pandas.io.sql as pd_sql
import sqlite3 as sql

con = sql.connect("test.db")
df = pd.DataFrame({'TestData': [1, 2, 3, 4, 5, 6, 7, 8, 9]}, dtype='float')
pd_sql.write_frame(df, "test_table2", con)
con.close()


con = sql.connect("test.db")
df2 = pd.read_sql_query("SELECT * from test_table2", con)
print df2.head()
con.close()