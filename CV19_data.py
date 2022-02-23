#!/usr/bin/env python
# coding: utf-8

# In[1]:


import csv;
import os;
import random;
import string;


# In[7]:


with open('People.csv', 'w', encoding='UTF8', newline='') as f:
    writer = csv.writer(f)
    
    # write the data
    for i in range(1, 1000001):
        x = random.randrange(0, 10000)
        y = random.randrange(0, 10000)  
        
        data = [i, x, y]
        writer.writerow(data)
        
    print("done");


# In[ ]:


with open('People_alt.csv', 'w', encoding='UTF8', newline='') as f:
    writer = csv.writer(f)
    
    # write the data
    for i in range(1, 101):
        x = random.randrange(0, 5000)
        y = random.randrange(0, 5000)  
        
        data = [i, x, y]
        writer.writerow(data)
        
    print("done");

