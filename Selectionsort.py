
# coding: utf-8

# In[12]:


#Álgoritmo de ordenación Selection Sort


import random


print("Ingrese cuantos numeros aleatorios desea obtener")
n=int(input())
arreglo = [random.randint(0,1000) for _ in range(n)]
print ("vector desordenado")
print(arreglo)


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

