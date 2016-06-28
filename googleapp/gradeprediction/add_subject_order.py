# -*- coding: utf-8 -*-
"""
Created on Fri Feb 19 16:55:54 2016

@author: Administrator
"""

import pandas as pd
import pandas.io.sql as pd_sql
import MySQLdb as sql
# import mysql.connector

df_file_all = pd.read_csv('CS_table_No2_No4_new.csv',delimiter=";", skip_blank_lines = True, 
                 error_bad_lines=False,encoding='utf8')

df_file_less = pd.read_csv('df_dropSub_less20.csv',delimiter=",", skip_blank_lines = True, 
                 error_bad_lines=False,encoding='utf8')
                 
df_file_all = df_file_all.drop(['STUDENTID','ACADYEAR','CAMPUSID','SEMESTER','CURRIC','CAMPUSNAME','SECTIONGROUP','GRADE'],axis=1)

subjects = []
countSub = 0
for sub in df_file_less['3COURSEID']:
    if sub not in subjects:
        subjects.append(sub)
        countSub = countSub+1
subjects.sort()

df_db = df_file_all[df_file_all["sub_id"].isin(subjects)]
df_db = df_db.drop_duplicates(['sub_id'], take_last=True)  
df_db = df_db.sort(['sub_id'])
   

# con = sql.connect(host='173.194.226.138', user='book',passwd = "1234", db = 'gradepredictiondb')
# cur = con.cursor()
# cur.execute( "SELECT * FROM mywebpage_subject")
#df = pd.DataFrame({'TestData': [1, 2, 3, 4, 5, 6, 7, 8, 9]}, dtype='float')
# #pd_sql.to_sql(df_db, "mywebpage_subject", con, index=False)
# con.close()

# print df_db.values

# for r in df_db.columns.values:
#     df_db[r] = df_db[r].map(str)
#     df_db[r] = df_db[r].map(str.strip)   
# #tuples = [tuple(x) for x in df_db.values]



# cnx = mysql.connector.connect(user='book', password='1234',
#                               host='173.194.226.138',
#                               database='gradepredictiondb')
# cursor = cnx.cursor()
# cnx.close()