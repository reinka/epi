
# coding: utf-8

# In[1]:

import numpy as np
import timeit
import matplotlib.pyplot as plt
get_ipython().magic('matplotlib inline')


# # Algorithmus

# In[2]:

def shakerSort(arr):
    swap = range(len(arr)-1)
    while 1:
        for index in (swap,reversed(swap)):
            swapped = False
            for i in index:
                if arr[i] > arr[i+1]:
                    arr[i], arr[i+1] = arr[i+1], arr[i]
                    swapped = True
            if not swapped:
                return arr
            
# Speicherkomplexität: O(n) 


# # Laufzeitkomplexität O(n²)

# In[3]:

random_number_sequence = np.arange(1,10000000)


# In[4]:

test_array = []
for i in range(1,15):
    test_array.append(np.random.choice(random_number_sequence, size=1500*i, replace=False))
test_array


# In[5]:

def laufzeiten(arr):
    laufzeiten = {}
    for i in range(14):
        laufzeit_arr = []
        start = timeit.default_timer()
        shakerSort(test_array[i])
        laufzeit_arr.append(timeit.default_timer() - start)        #Differenz Start-/Stopzeit als Element im Array
        laufzeiten[i] = laufzeit_arr                                   #Array ins Dict einfügen  

    
    #Berechne Mittelwert der Laufzeiten   
    mean = []
    for value in laufzeiten.values():
        mean.append(np.mean(value))
    return (mean)


# In[16]:

x = laufzeiten(test_array)
x


# In[8]:

y_1 = np.array([0.00065113000164274126,
 0.0012003619995084591,
 0.0017963179998332635,
 0.0054668260054313578,
 15.964041726001597,
 34.208830466996005,
 47.93599814800109,
 62.170872569004132,
 77.059121206999407,
 92.270028195001942,
 111.71400923500187,
 130.2647078969967,
 153.23558610799955,
 174.79504887200164])

n = []
for i in range(1,len(y_1)+1):
    n.append(1500*i)
    
x_1 = np.array(n)
x_1


# In[10]:

#import sys            for Python 2.7

#reload(sys)  
#sys.setdefaultencoding('utf8')

# get x and y vectors
x = x_1
y = y_1

# calculate polynomial
z = np.polyfit(x, y, 2)
f = np.poly1d(z)

# calculate new x's and y's
x_new = np.linspace(x[0], x[-1], 50)
y_new = f(x_new)

plt.plot(x,y,'o', x_new, y_new)
plt.title(r'Shakersort Laufzeitkomplexität')
plt.xlabel(r'Array Elemente $\mathrm{n}$')
plt.ylabel('Laufzeit')
plt.xlim([x[0]-1, x[-1]*1.1])
plt.savefig('Shakersort Laufzeitkomplexität')
plt.show()


# In[ ]:




# In[ ]:



