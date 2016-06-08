## -*- coding: utf-8 -*-
#"""
#Created on Tue May 10 17:19:14 2016
#
#@author: Methinee
#"""
import pandas as pd
import numpy as np
import pickle
import xlwt
import matplotlib.pyplot as plt

#
#
#
##----------------------Traning Data With Merging-----------------------
##df_file = pd.read_csv('../data/df_more20.csv',delimiter=",", skip_blank_lines = True, 
##                 error_bad_lines=False)
#df_acc = pd.read_csv('../src/compare_accuracy.csv',delimiter=",", skip_blank_lines = True, 
#                 error_bad_lines=False)
#                 
#df_train = pd.read_csv('../src/compare_trainingData.csv',delimiter=",", skip_blank_lines = True, 
#                 error_bad_lines=False)
#                 
#df_class = pd.read_csv('../src/compare_class.csv',delimiter=",", skip_blank_lines = True, 
#                 error_bad_lines=False)
#
df_all = pd.read_csv('../src/compare_all.csv',delimiter=",", skip_blank_lines = True, 
                 error_bad_lines=False)

headers=list(df_all.columns.values)
subjects = []
#Create dictionary of list subjects
for sub in df_all[headers[0]]:
    subjects.append(sub)

classes = []
#Create dictionary of list subjects
for c in df_all[headers[1]]:
    classes.append(c)


accuracy = []
#Create dictionary of list subjects
for acc in df_all[headers[2]]:
    accuracy.append(acc)
    
train = []
#Create dictionary of list subjects
for tr in df_all[headers[3]]:
    train.append(tr)    


#n_groups = 15
#
#std_men = (3, 5, 2, 3, 3,3, 5, 2, 3, 3,3, 5, 2, 3, 3)
#
#std_women = (3, 5, 2, 3, 3,3, 5, 2, 3, 3,3, 5, 2, 3, 3)
#
#
#index = np.arange(n_groups)
#bar_width = 0.20
#
#opacity = 0.7
#error_config = {'ecolor': '0.3'}

#rects1 = plt.bar(index,df_all[headers[1]][:15], bar_width,
#                 alpha=opacity,
#                 color='b',
#                 
#                 error_kw=error_config,
#                 label='#Class')
#
#rects2 = plt.bar(index + bar_width, df_all[headers[3]][:15], bar_width,
#                 alpha=opacity,
#                 color='r',
#                 yerr=std_women,
#                 error_kw=error_config,
#                 label='#Training Data')
#                 
#rects3 = plt.bar(index + bar_width+bar_width, df_all[headers[2]][:15], bar_width,
#                 alpha=opacity,
#                 color='g',
#                 yerr=std_women,
#                 error_kw=error_config,
#                 label='#Accuracy')
#                 
#
#for rect in rects1:
#    height = rect.get_height()
#    plt.text(rect.get_x()+rect.get_width()/2., 1.05*height, '%d'%int(height),
#            ha='center', va='bottom')
#            
#for rect in rects2:
#    height = rect.get_height()
#    plt.text(rect.get_x()+rect.get_width()/2., 1.05*height, '%d'%int(height),
#            ha='center', va='bottom')
#            
#for rect in rects3:
#    height = rect.get_height()
#    plt.text(rect.get_x()+rect.get_width()/2., 1.05*height, '%d'%int(height),
#            ha='center', va='bottom')
#
#
#plt.xlabel('Subject')
#plt.ylabel('Scores')
#plt.title('Scores of #Traing Data and #Class')
#plt.xticks(index + bar_width, subjects[:15])
#plt.legend()
#
#plt.tight_layout()
#plt.show()
#

#//////////////////////////////////////////////////////////////////////////////////////////////////
#rects1 = plt.bar(index,df_all[headers[1]][95:110], bar_width,
#                 alpha=opacity,
#                 color='b',
#                 
#                 error_kw=error_config,
#                 label='#Class')
#
#rects2 = plt.bar(index + bar_width, df_all[headers[3]][95:110], bar_width,
#                 alpha=opacity,
#                 color='r',
#                 yerr=std_women,
#                 error_kw=error_config,
#                 label='#Training Data')
#                 
#rects3 = plt.bar(index + bar_width+bar_width, df_all[headers[2]][95:110], bar_width,
#                 alpha=opacity,
#                 color='g',
#                 yerr=std_women,
#                 error_kw=error_config,
#                 label='#Accuracy')
#                 
#
#for rect in rects1:
#    height = rect.get_height()
#    plt.text(rect.get_x()+rect.get_width()/2., 1.02*height, '%d'%int(height),
#            ha='center', va='bottom')
#            
#for rect in rects2:
#    height = rect.get_height()
#    plt.text(rect.get_x()+rect.get_width()/2., 1.02*height, '%d'%int(height),
#            ha='center', va='bottom')
#            
#for rect in rects3:
#    height = rect.get_height()
#    plt.text(rect.get_x()+rect.get_width()/2., 1.02*height, '%d'%int(height),
#            ha='center', va='bottom')
#
#
#plt.xlabel('Subject')
#plt.ylabel('Scores')
##plt.title('Scores of #Traing Data and #Class')
#plt.xticks(index + bar_width, subjects[:15])
#plt.legend()
#
#plt.tight_layout()
#plt.show()

#///////////////////////////////////////////////////////////////////////////////////////

column = 6
row = 300
z = np.zeros((row,column))
for d in xrange(len(train)):
    for i in xrange(row):
        for j in xrange(column):
            if j == classes[d] and i == train[d]:
                z[i][j] = accuracy[d]
                print " hello"
                
print z


#dx, dy = 0.15, 0.05
y, x = np.mgrid[slice(0, 300),slice(0, 6)]
#plt.subplot()
#plt.pcolormesh(x, y, z,shading='gouraud', cmap='jet')
plt.pcolor(x, y, z, cmap='jet')
#plt.title('pcolor')
#plt.xticks(np.arange(min(x), max(x), 1.50))
## set the limits of the plot to the limits of the data
#plt.colorbar()
#plt.axis([x.min(), x.max(), y.min(), y.max()])


plt.yticks(np.arange(0, 300, 50.0),label="#Training Data")
plt.xticks(np.arange(0, 6, 1.0),label='#Class')
plt.colorbar()

