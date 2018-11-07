
# coding: utf-8

# In[3]:


import random

print("Ingrese cuantos numeros aleatorios desea obtener")
n=int(input())
vector = [random.randint(0,1000) for _ in range(n)]
print ("vector desordenado")
print(vector)

def bubble_sort(vector):
    permutation = True
    iteración = 0
    while permutation == True:
        permutation = False
        iteración = iteración + 1
        for actual in range(0, len(vector) - iteración):
            if vector[actual] > vector[actual + 1]:
                permutation = True
                # Intercambiamos los dos elementos
                vector[actual], vector[actual + 1] = vector[actual + 1],vector[actual]
    return vector  

bubble_sort(vector)
print ("vector desordenado")
print(vector)

def test():
    start = time.clock()
    bubble_sort(vector)
    elapsed = (time.clock() - start)
    print("Tiempo esperado para Bubble_Sort = ", elapsed)

if __name__ == '__main__':
    import time
test() 

