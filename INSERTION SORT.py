#!/usr/bin/env python
# coding: utf-8

# In[12]:


import random


print("Ingrese cuantos numeros aleatorios desea obtener")
n=int(input())
alist = [random.randint(0,1000) for _ in range(n)]
print "vector desordenado"
print(alist)

def insertionSort(alist):
    
   for index in range(1,len(alist)):

     currentvalue = alist[index]
     position = index

     while position>0 and alist[position-1]>currentvalue:
         alist[position]=alist[position-1]
         position = position-1

     alist[position]=currentvalue

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




