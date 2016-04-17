# -*- coding: utf-8 -*-
"""
Created on Tue Mar 29 22:44:14 2016

@author: Methinee
"""
import pandas as pd
import numpy as np
import pickle

for i in range(0,5):
    f = open("train/dataset%02d.pic"%(i), 'rb')   # 'rb' for reading binary file
    mydict = "mydict%02d"%(i)
    mydict = pickle.load(f)
    f.close()             