#!/usr/bin/env python
# coding: utf-8

# In[36]:


import csv;
import os;
import random;
import string;


# In[7]:


# with open('People.csv', 'w', encoding='UTF8', newline='') as f:
#     writer = csv.writer(f)
    
#     # write the data
#     for i in range(1, 1000001):
#         x = random.randrange(0, 10000)
#         y = random.randrange(0, 10000)  
        
#         data = [i, x, y]
#         writer.writerow(data)
        
#     print("done");
# with open('People_alt.csv', 'w', encoding='UTF8', newline='') as f:
#     writer = csv.writer(f)
    
#     # write the data
#     for i in range(1, 101):
#         x = random.randrange(0, 5000)
#         y = random.randrange(0, 5000)  
        
#         data = [i, x, y]
#         writer.writerow(data)
        
#     print("done");


# In[39]:


# open the file in the write mode
f = open('People.csv', 'w', encoding='UTF8', newline='')
fs = open('S-Infected.csv', 'w', encoding='UTF8', newline='')
fl = open('L-Infected.csv', 'w', encoding='UTF8', newline='')

# create the csv writer
writeNorm = csv.writer(f)
writeInfectedS = csv.writer(fs)
writeInfectedL = csv.writer(fl)

# write a row to the csv file
for i in range(1, 1000001):
    k = random.uniform(0,1)
    x = random.randrange(0, 10000)
    y = random.randrange(0, 10000)
    data = [i, x, y]
    if k<= 0.001:
        writeInfectedS.writerow(data)
    elif k<= 0.01:
        writeInfectedL.writerow(data)
    else:
        writeNorm.writerow(data)

# close the file
f.close()
fs.close()
fl.close()


# In[33]:


# open the file in the write mode
f = open('People_alt.csv', 'w', encoding='UTF8', newline='')
fs = open('S-Infected_alt.csv', 'w', encoding='UTF8', newline='')
fl = open('L-Infected_alt.csv', 'w', encoding='UTF8', newline='')

# create the csv writer
writeNorm = csv.writer(f)
writeInfectedS = csv.writer(fs)
writeInfectedL = csv.writer(fl)

# write a row to the csv file
for i in range(1, 101):
    k = random.uniform(0,1)
    x = random.randrange(0, 5000)
    y = random.randrange(0, 5000)
    data = [i, x, y]
    if k<0.05:
        writeInfectedS.writerow(data)
    elif k<0.3:
        writeInfectedL.writerow(data)
    else:
        writeNorm.writerow(data)

# close the file
f.close()
fs.close()
fl.close()

