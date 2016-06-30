# -*- coding: utf-8 -*-
"""
Created on Sun May 29 20:49:37 2016

@author: Methinee
"""
import pandas as pd

df_file = pd.read_csv('../data/df_dropSub_less20.csv',delimiter=",", skip_blank_lines = True, 
                 error_bad_lines=False)
                 
drop_naResult = df_file[df_file['4RESULT'] != 0]
drop_naResult.to_csv('../data'+'/df_dropSub_less20_dropNaResult.csv')