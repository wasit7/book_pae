# -*- coding: utf-8 -*-
"""
Created on Thu Feb 18 21:51:57 2016

@author: Administrator
"""
import csv, sqlite3
import pandas as pd

import sqlite3

conn = sqlite3.connect('subject.sqlite')
print "Opened database successfully";

conn.execute('''CREATE TABLE Subject
       (sub_id INT PRIMARY KEY     NOT NULL,
       sub_name           TEXT    NOT NULL,
       credit        INT     NOT NULL);''')
print "Table created successfully";

conn.close()