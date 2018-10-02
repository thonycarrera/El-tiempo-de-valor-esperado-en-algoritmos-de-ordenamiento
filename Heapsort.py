
# coding: utf-8

# In[13]:


#Álgoritmo de ordenación HeapSort

def heapify(arreglo, n, i): 
    mayor = i 
    izquierda = 2 * i + 1  
    derecha = 2 * i + 2  
 
    if izquierda < n and arreglo[i] < arreglo[izquierda]: 
        mayor = izquierda

    if derecha < n and arreglo[mayor] < arreglo[derecha]: 
        mayor = derecha 

    if mayor != i: 
        arreglo[i],arreglo[mayor] = arreglo[mayor],arreglo[i]
 
        heapify(arreglo, n, mayor) 
 
def heapSort(arreglo): 
    n = len(arreglo) 
    
    for i in range(n, -1, -1): 
        heapify(arreglo, n, i) 
 
    for i in range(n-1, 0, -1): 
        arreglo[i], arreglo[0] = arreglo[0], arreglo[i] 
        heapify(arreglo, i, 0) 
        
arreglo = [45,62,39,71,63,13,168,888,473,43442,254,534,12,332,243,980,11,8998,1020,77]
heapSort(arreglo)
print ("El arreglo ordenado es")
print(arreglo)

def prueba():
                    start = time.clock()
                    heapSort(arreglo)
                    elapsed = (time.clock() - start)
                    print ("  ", elapsed)

if __name__ == '__main__':
    import time
    prueba()

