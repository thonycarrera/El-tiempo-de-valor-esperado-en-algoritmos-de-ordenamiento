
# coding: utf-8

# In[20]:


#Álgoritmo de ordenación Selection Sort

def selectionSort(arreglo):
   for llenar_ranura in range(len(arreglo)-1,0,-1):
       posición_de_máximo=0
       for locación in range(1,llenar_ranura+1):
           if arreglo[locación]>arreglo[posición_de_máximo]:
               posición_de_máximo = locación

       aux = arreglo[llenar_ranura]
       arreglo[llenar_ranura] = arreglo[posición_de_máximo]
       arreglo[posición_de_máximo] =aux 

print("El arreglo ordenado es:")
arreglo = [54,26,93,17,77,31,55,20,4324,67456,4434,44,4411,856,644,533,63,774,6465,33]
selectionSort(arreglo)
print(arreglo)

def prueba():
                    start = time.clock()
                    selectionSort(arreglo)
                    elapsed = (time.clock() - start)
                    print ("  ", elapsed)

if __name__ == '__main__':
    import time
    prueba()

