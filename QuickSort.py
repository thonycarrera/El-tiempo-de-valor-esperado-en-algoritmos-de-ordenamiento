
# coding: utf-8

# In[14]:


def quick_sort(vector):
     if not vector:
        return []
     else:
        pivote = vector[-1]
        menor = [x for x in vector     if x <  pivote]
        mas_grande = [x for x in vector[:-1] if x >= pivote]
        return quick_sort(menor) + [pivote] + quick_sort(mas_grande)
    
vec = [15,26,93,17,77,923,44,1,20,89,950,32,18,122,9,14,190]
quick_sort(vec)
print(vec)

def test():
    start = time.clock()
    quick_sort(vec)
    elapsed = (time.clock() - start)
    print("Tiempo esperado para Quick_Sort = " , elapsed)

if __name__ == '__main__':
    import time
test() 

