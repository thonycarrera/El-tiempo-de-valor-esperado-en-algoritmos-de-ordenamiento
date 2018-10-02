#!/usr/bin/env python
# coding: utf-8

# In[7]:


def insertionSort(vector):
   for index in range(1,len(vector)):

     currentvalue = vector[index]
     position = index

     while position>0 and vector[position-1]>currentvalue:
         vector[position]=vector[position-1]
         position = position-1

     vector[position]=currentvalue

vector = [54,26,93,17,77,31,44,55,20,89,90,32,18,122,9,14,190]
insertionSort(alist)
print(alist)


# In[ ]:





# In[ ]:




