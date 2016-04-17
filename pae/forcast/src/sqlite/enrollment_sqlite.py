# -*- coding: utf-8 -*-
"""
Created on Thu Feb 18 22:16:43 2016

@author: Administrator
"""

import sqlite3

conn = sqlite3.connect('enrollment.sqlite')
print "Opened database successfully";

conn.execute('''CREATE TABLE Enrollment
       (std_id INT PRIMARY KEY     NOT NULL,
       sub_id           TEXT    ,
       grade            INT     ,
       term        INT,
       year         INT);''')
print "Table created successfully";

conn.close()