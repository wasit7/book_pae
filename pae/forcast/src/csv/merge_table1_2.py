# -*- coding: utf-8 -*-
"""
Created on Wed May 04 11:34:19 2016

@author: Methinee
"""
import pandas as pd

df_first = pd.read_excel('../../src/transform.xlsx')

df_second = pd.read_csv('../../data/CS_table_No1.csv',delimiter=";", skip_blank_lines = True, 
                 error_bad_lines=False)
df_second = df_second.drop(['ADMITYEAR','STUDENTSTATUS','STUDENTSTATUSNAME','PROVINCENAME','BIRTHDATE'],axis=1)

result = pd.merge(df_first, df_second, on=['0STUDENTID'])


writer = pd.ExcelWriter("../../data/transform_merge.xlsx")
pd.DataFrame(result).to_excel(writer,"schoolGpa&province")
writer.save()