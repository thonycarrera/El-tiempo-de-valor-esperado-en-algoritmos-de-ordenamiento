#!/usr/bin/env python
# coding: utf-8

# In[1]:


def insertionSort(alist):
    
   for index in range(1,len(alist)):

     currentvalue = alist[index]
     position = index

     while position>0 and alist[position-1]>currentvalue:
         alist[position]=alist[position-1]
         position = position-1

     alist[position]=currentvalue

alist = [54,26,93,17,77,31,44,55,20,23222,234,235,12,332,243,987,34,3443,55,78]
insertionSort(alist)
print "vector ordenado"
print(alist)

def test():
    start = time.clock()
    insertionSort(alist)
    elapsed = (time.clock() - start)
    print "Tiempo esperado para Insertion_Sort = ", elapsed

if __name__ == '__main__':
    import time
    test() 


# In[ ]:





# In[ ]:





# In[ ]:




