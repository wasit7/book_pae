# -*- coding: utf-8 -*-
"""
Created on Sat Nov 28 21:51:46 2015

@author: Methinee
"""

#http://pandas.pydata.org/pandas-docs/stable/visualization.html
import pandas as pd

xl = pd.ExcelFile('../data/CS_table_No1.xls')
#xl.sheet_names  # see all sheet names
table1=xl.parse(xl.sheet_names[0],index_col='STUDENTID')  # read a specific sheet to DataFrame
#table1.convert_objects(convert_numeric=True)
table1.SCHOOLGPA[1:].plot()    # found higher gpa in 470000
#table1.SCHOOLGPA[1:].plot(logy=True,legend=True)   # found lower gpa in 360000


# edit in xls already!!