
# coding: utf-8

# In[13]:



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
                vector[actual], vector[actual + 1] =                 vector[actual + 1],vector[actual]
    return vector  
vector = [15,26,93,17,77,923,44,1,223,89,950,32,168,122,9,14,190,456,6777]
bubble_sort(vector)
print(vector)

def test():
    start = time.clock()
    bubble_sort(vector)
    elapsed = (time.clock() - start)
    print("Tiempo esperado para Bubble_Sort = ", elapsed)

if __name__ == '__main__':
    import time
test() 

