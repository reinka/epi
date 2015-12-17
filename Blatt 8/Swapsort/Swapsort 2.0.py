
# coding: utf-8

# In[1]:

import random
import numpy as np

import matplotlib.pyplot as plt
get_ipython().magic('matplotlib inline')


# # SWAPSORT IMPLEMENTIERUNG

# In[2]:

def swap_sort(arr):
    index = 0
    while index < len(arr) - 1:
        new_index = sum(x < arr[index] for x in arr)
        if index == new_index:
            index += 1
        else:
            arr[index], arr[new_index] = arr[new_index], arr[index]
    #return arr
    
#Luafzeit und Speicherkomplexität: O(n)


# In[3]:

arr = [7,8,5,2,4,9,3,1]
arr


# In[4]:

swap_sort(arr)


# # Zeitkomplexität

# In[5]:

random_number_sequence = np.arange(1,10000000)


# ## Sample arrays mit 500, 1000, 1.500, 2.000, 2.500 & 3.000 zufällig ausgewählten Elementen
# 

# In[36]:

test_array = []
for i in range(1,11):
    test_array.append(np.random.choice(random_number_sequence, size=200*i, replace=False))


# ## Laufzeitbestimmung 

# In[37]:

import timeit


laufzeiten = {}
for i in range(10):
    laufzeit_arr = []
    start = timeit.default_timer()
    swap_sort(test_array[i])
    laufzeit_arr.append(timeit.default_timer() - start)        #Differenz Start-/Stopzeit als Element im Array
    laufzeiten[i] = laufzeit_arr                                   #Array ins Dict einfügen  

print (laufzeiten)
    
#Berechne Mittelwert der Laufzeiten   
mean = []
for value in laufzeiten.values():
    mean.append(np.mean(value))
mean


# In[42]:

n = []
for i in range(1,11):
    n.append(200*i)

# get x and y vectors
x = n
y = mean

# calculate polynomial
z = np.polyfit(x, y, 2)
f = np.poly1d(z)

# calculate new x's and y's
x_new = np.linspace(x[0], x[-1], 50)
y_new = f(x_new)

plt.plot(x,y,'o', x_new, y_new)
plt.title(r'Swapsort Laufzeitkomplexität')
plt.xlabel(r'Array Elemente $\mathrm{n}$')
plt.ylabel('Zeit $\mathrm{t}$')
plt.xlim([x[0]-1, x[-1]*1.1])
plt.savefig('Swapsort Laufzeitkomplexität')
plt.show()


# In[ ]:



