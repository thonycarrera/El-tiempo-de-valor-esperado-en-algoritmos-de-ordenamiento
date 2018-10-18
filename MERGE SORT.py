#!/usr/bin/env python
# coding: utf-8

# In[13]:


import random

print("Ingrese cuantos numeros aleatorios desea obtener")
n=int(input())
alist = [random.randint(0,1000) for _ in range(n)]
print "vector desordenado"
print(alist)

def merge(arr, l, m, r): 
    n1 = m - l + 1
    n2 = r- m 
  
    # create temp arrays 
    L = [0] * (n1) 
    R = [0] * (n2) 
  
    
    for i in range(0 , n1): 
        L[i] = arr[l + i] 
  
    for j in range(0 , n2): 
        R[j] = arr[m + 1 + j] 
  
    i = 0     
    j = 0     
    k = l     
  
    while i < n1 and j < n2 : 
        if L[i] <= R[j]: 
            arr[k] = L[i] 
            i += 1
        else: 
            arr[k] = R[j] 
            j += 1
        k += 1
  
    while i < n1: 
        arr[k] = L[i] 
        i += 1
        k += 1

    while j < n2: 
        arr[k] = R[j] 
        j += 1
        k += 1
  
def mergeSort(arr,l,r): 
    if l < r: 
        m = (l+(r-1))/2
        mergeSort(arr, l, m) 
        mergeSort(arr, m+1, r) 
        merge(arr, l, m, r) 

arr = alist 
n = len(arr)
  
mergeSort(arr,0,n-1) 
print ("\nVector ordenado") 
for i in range(n): 
    print ("%d" %arr[i]),
    
def test():
    start = time.clock()
    mergeSort(arr,0,n-1) 
    elapsed = (time.clock() - start)
    print "\n\nTiempo esperado para Merge_Sort = ", elapsed

if __name__ == '__main__':
    import time
    test() 


# In[ ]:





# In[ ]:





# In[ ]:




