# -*- coding: utf-8 -*-
"""
Created on Wed Apr 13 23:36:10 2016

@author: Administrator
"""

import xlwt 

book = xlwt.Workbook(encoding="utf-8") 

sheet1 = book.add_sheet("Python Sheet 1") 
sheet2 = book.add_sheet("Python Sheet 2") 
sheet3 = book.add_sheet("Python Sheet 3") 

sheet1.write(0, 0, "This is the First Cell of the First Sheet") 
sheet2.write(0, 0, "This is the First Cell of the Second Sheet") 
sheet3.write(0, 0, "This is the First Cell of the Third Sheet") 
sheet2.write(1, 10, "This is written to the Second Sheet") 
sheet3.write(0, 2, "This is part of a list of information in the Third Sheet") 
sheet3.write(1, 2, "This is part of a list of information in the Third Sheet") 
sheet3.write(2, 2, "This is part of a list of information in the Third Sheet") 
sheet3.write(3, 2, "This is part of a list of information in the Third Sheet") 

book.save("python_spreadsheet.xls")