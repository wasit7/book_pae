# -*- coding: utf-8 -*-
"""
Created on Sun Nov 15 14:32:26 2015

@author: Administrator
"""

import csv, sqlite3

con = sqlite3.connect("../sqlite/test")
cur = con.cursor()
cur.execute("CREATE TABLE 'testSqlite1' ('policyID', 'statecode', 'county', 'eq_site_limit');")
with open('../sqlite/test.csv','rb') as fin:
    dr = csv.DictReader(fin) # comma is default delimiter
    to_db = [(i['policyID'], i['statecode'], i['county'], i['eq_site_limit']) for i in dr]
cur.executemany("INSERT INTO 'testSqlite1' (policyID, statecode, county, eq_site_limit) VALUES (?, ?, ?, ?);", to_db)
con.commit()

