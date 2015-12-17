
# coding: utf-8

# In[28]:

import timeit
import numpy as np
from numpy.random import randint
import pandas as pd 
from pandas import Series, DataFrame

import matplotlib.mlab as mlab
import matplotlib.pyplot as plt

from scipy.stats import norm
import seaborn as sns

import sys  

reload(sys)  
sys.setdefaultencoding('utf8')

from IPython.display import display, HTML
get_ipython().magic(u'matplotlib inline')


# # PART 1: COUNTINGSORT IMPLEMENTIERUNG
# 

# In[57]:

def countingsort(arr):
    
    #Umwandlung in Pandas.Series für Histogrammbildung
    hist = Series(arr)
    sns.distplot(hist,kde=False,rug=True,color='royalblue', bins=max(hist.index)*3, label=r'Häufigkeit')
    plt.ylim(0, max(hist.index)+1)
    plt.xlabel('Element')
    plt.ylabel(r'Häufigkeit')
    plt.title(r'$\mathrm{Array\ Histogram}$')
    plt.show()
    
    
    
    #Sortiertes Histogramm, fehlende Werte (NaN) werden durch 0 ersetzt
    sorted_hist = hist.value_counts().sort_index()
    cleaned_hist = Series(sorted_hist, index=range(max(sorted_hist.index)+1)).fillna(0)

    
    #Aufsummierung der Werte im Histogramm
    summed_hist = Series(cleaned_hist.cumsum()[:-1].values, index=range(1, max(arr)+1))
    
    #Bereinigung des summierten Histogramms
    summed_hist_cleaned = Series(summed_hist, index=range(max(arr)+1)).fillna(0)
    
    
    
    
    #Kreiere DataFrames zu A, B und Hilfsarray C
    
    #DataFrame A
    rows = len(arr)            #Anzahl Reihen
    columns_A = []             #Anzahl Spalten
    
    #Benenne die Spalten für A
    for num in range(rows):
        columns_A.append('A[' + str(num) + ']')
        
    #Kreiere DataFrame
    dframe_A = DataFrame(np.array(list(arr)*rows).reshape(rows, rows), columns=columns_A, index=range(rows))
    
    
    #Das Gleiche nun für Hilfsarray C
    hilfs_array = np.array(summed_hist_cleaned.values)
    columns = len(hilfs_array)
    columns_C = []
    for num in range(columns):
        columns_C.append('C[' + str(num) + ']')
    dframe_C = DataFrame(np.array(list(hilfs_array)*rows).reshape(rows ,columns), index=range(rows), columns=columns_C)
    
    
    #Fertige zunächst LEERES DataFrame B an
    columns_B = []
    for num in range(rows):
        columns_B.append('B[' + str(num) + ']')    

    dframe_B = DataFrame(np.nan, index=range(rows),columns=columns_B).fillna(' ')
    
    
    #Kreiere Dict, in dem Keys und Values für das später fertig sortierte Array B angelegt werden 
    b = {}
    lookup_value = 0
    for i in range(rows):
        #Iteration der Werte in C sobald in A nachgeschlagen 
        if i > 0:
            dframe_C['C['+str(lookup_value)+']'][i:] += 1
        
        #Wert, der in C nachgeschlagen, und in B an Stelle C[A[i]] eingefügt werden soll
        lookup_value = dframe_A.values[i][i]
        key = 'B[' + str(int(dframe_C.values[i][lookup_value])) + ']'
        b[key] = [lookup_value,i]
    
    
    #Füge Werte schließlich sortiert in B ein
    for key, value in b.items():
        dframe_B[key][value[1]:] = value[0]    
    
    #Konkatenieren der 3 DataFrames
    final_dframe = pd.concat([dframe_A, dframe_C, dframe_B], axis=1)
    
    
    #Sortiertes Array B
    result = []
    for i in range(len(b)):
        result.append(b['B[' + str(i) + ']'][0])

    #print('\nDataFrame A\n')
    #display(dframe_A)
    #print('\nDataFrame C\n')
    #display(dframe_C)
    #print('\nDataFrame B\n')
    #display(dframe_B)
    
    #display(final_dframe)
    
    return result



# # Testläufe
# 

# In[10]:

countingsort([2,5,3,0,2,3,0,3])


# In[60]:

countingsort(randint(0,100,100))


# # Segemente des Codes

# In[457]:

arr = [2,5,3,0,2,3,0,3]
arr


# In[458]:

hist = Series(arr)
hist
sorted_hist = hist.value_counts().sort_index()


# In[459]:

sorted_hist


# In[460]:

cleaned_hist = Series(sorted_hist, index=range(max(sorted_hist.index)+1))
cleaned_hist


# In[461]:

cleaned_hist.cumsum()[:-1].values


# In[462]:

summed_hist = Series(cleaned_hist.cumsum()[:-1].values, index=range(1, max(arr)+1))


# In[463]:

summed_hist_cleaned = Series(summed_hist, index=range(max(arr)+1)).fillna(0)
summed_hist_cleaned


# In[194]:

dframe = DataFrame(np.array(arr*8).reshape(8,8), columns=range(len(arr)), index=range(len(arr)))
dframe


# In[384]:

hilfs_array = np.array(summed_hist_cleaned.values)
hilfs_array


# In[392]:

rows = len(arr)
columns_A = []
for num in range(rows):
    columns_A.append('A[' + str(num) + ']')

dframe_A = DataFrame(np.array(arr*len(arr)).reshape(rows, rows), columns=columns_A, index=range(rows))
dframe_A


# In[393]:

columns = len(hilfs_array)
columns_C = []
for num in range(columns):
    columns_C.append('C[' + str(num) + ']')

dframe_C = DataFrame(np.array(list(hilfs_array)*8).reshape(rows ,columns), index=range(rows), columns=columns_C)
dframe_C


# In[394]:

b = {}
lookup_value = 0
for i in range(rows):
    if i > 0:
        dframe_C['C['+str(lookup_value)+']'][i:] += 1
    lookup_value = dframe_A.values[i][i]
    key = 'B[' + str(int(dframe_C.values[i][lookup_value])) + ']'
    b[key] = [lookup_value,i]
    
dframe_C
    


# In[395]:

columns_B = []
for num in range(rows):
    columns_B.append('B[' + str(num) + ']')    

dframe_B = DataFrame(np.nan, index=range(rows),columns=columns_B).fillna(' ')
for key, value in b.items():
    dframe_B[key][value[1]:] = value[0]
dframe_B


# In[396]:

result = pd.concat([dframe_A, dframe_C, dframe_B], axis=1)
result


# In[450]:

hist = Series(arr)
sns.distplot(hist,kde=False,rug=True,color='royalblue', bins=max(hist.index)*3, label='Häufigkeit')
plt.ylim(0, max(hist.index)+1)
plt.xlabel('Element')
plt.ylabel('Häufigkeit')
plt.title(r'$\mathrm{Array\ Histogram}$')
plt.show()


# # PART 2: LAUFZEITBESTIMMUNG 
# 
# ### Überflüssige Operationen in der Funktion werden für Laufzeitmessung weg-kommentiert

# In[61]:

def countingsort_laufzeit(arr):
    
    #Umwandlung in Pandas.Series für Histogrammbildung
    hist = Series(arr)
    #sns.distplot(hist,kde=False,rug=True,color='royalblue', bins=max(hist.index)*3, label='Häufigkeit')
    #plt.ylim(0, max(hist.index)+1)
    #plt.xlabel('Element')
    #plt.ylabel('Häufigkeit')
    #plt.title(r'$\mathrm{Array\ Histogram}$')
    #plt.show()
    
    
    
    #Sortiertes Histogramm, fehlende Werte (NaN) werden durch 0 ersetzt
    sorted_hist = hist.value_counts().sort_index()
    cleaned_hist = Series(sorted_hist, index=range(max(sorted_hist.index)+1)).fillna(0)

    
    #Aufsummierung der Werte im Histogramm
    summed_hist = Series(cleaned_hist.cumsum()[:-1].values, index=range(1, max(arr)+1))
    
    #Bereinigung des summierten Histogramms
    summed_hist_cleaned = Series(summed_hist, index=range(max(arr)+1)).fillna(0)
    
    
    
    
    #Kreiere DataFrames zu A, B und Hilfsarray C
    
    #DataFrame A
    rows = len(arr)            #Anzahl Reihen
    columns_A = []             #Anzahl Spalten
    
    #Benenne die Spalten für A
    for num in range(rows):
        columns_A.append('A[' + str(num) + ']')
        
    #Kreiere DataFrame
    dframe_A = DataFrame(np.array(list(arr)*rows).reshape(rows, rows), columns=columns_A, index=range(rows))
    
    
    #Das Gleiche nun für Hilfsarray C
    hilfs_array = np.array(summed_hist_cleaned.values)
    columns = len(hilfs_array)
    columns_C = []
    for num in range(columns):
        columns_C.append('C[' + str(num) + ']')
    dframe_C = DataFrame(np.array(list(hilfs_array)*rows).reshape(rows ,columns), index=range(rows), columns=columns_C)
    
    
    #Fertige zunächst LEERES DataFrame B an
    #columns_B = []
    #for num in range(rows):
    #    columns_B.append('B[' + str(num) + ']')    

    #dframe_B = DataFrame(np.nan, index=range(rows),columns=columns_B).fillna(' ')
    
    
    #Kreiere Dict, in dem Keys und Values für das später fertig sortierte Array B angelegt werden 
    b = {}
    lookup_value = 0
    for i in range(rows):
        #Iteration der Werte in C sobald in A nachgeschlagen 
        if i > 0:
            dframe_C['C['+str(lookup_value)+']'][i:] += 1
        
        #Wert, der in C nachgeschlagen, und in B an Stelle C[A[i]] eingefügt werden soll
        lookup_value = dframe_A.values[i][i]
        key = 'B[' + str(int(dframe_C.values[i][lookup_value])) + ']'
        b[key] = [lookup_value,i]
        
    result = []
    for i in range(len(b)):
        if b['B[' + str(i) + ']'][0]:
            result.append(b['B[' + str(i) + ']'][0])
          
    
    #Füge Werte schließlich sortiert in B ein
    #for key, value in b.items():
    #    dframe_B[key][value[1]:] = value[0]    
    
    #Konkatenieren der 3 DataFrames
    #final_dframe = pd.concat([dframe_A, dframe_C, dframe_B], axis=1)

    #print('\nDataFrame A\n')
    #display(dframe_A)
    #print('\nDataFrame C\n')
    #display(dframe_C)
    #print('\nDataFrame B\n')
    #display(dframe_B)
    
    #display(final_dframe)
    
    return result




# # Laufzeitenmessung
# 
# ####  Es werden Arrays mit 10, 100, 1.000, und 10.000 Elemente eingelesen. Anschließend wird jeweils über 10 Laufzeiten gemittelt.  

# In[65]:

laufzeiten = {}
arr = [randint(0,1000,10),
       randint(0,1000,100),
       randint(0,1000,1000), 
       randint(0,1000,10000),
       randint(0,1000,100000)]

for i in range(4):
    n = 0
    laufzeit_arr = []
    while(n <10):
        start = timeit.default_timer()
        countingsort_laufzeit(arr[i])
        laufzeit_arr.append(timeit.default_timer() - start)
        n+=1
    laufzeiten[i] = laufzeit_arr

mean = []
for value in laufzeiten.values():
    mean.append(np.mean(value))


# # Gemittelte Laufzeiten für jeweils 10, 100, 1.000 & 10.000 Elemente

# In[66]:

mean


# # PLOT 

# In[67]:

n = [10,100,1000,10000]
plt.plot(mean,n[:len(mean)])
plt.title('Countingsort Laufzeitkomplexität')
plt.ylim(0,max(n)*1.2)
plt.xlim(0,max(mean)*1.2)
plt.xlabel('Laufzeit')
plt.ylabel(r'Anzahl der Elemente $\mathrm{n}$ ')
plt.savefig('Countingsort Laufzeitkomplexität')
plt.show()


# In[64]:

arr = randint(0,1000,100000)
laufzeit_extra = []
while(n <10):
    start = timeit.default_timer()
    countingsort_laufzeit(arr)
    laufzeit_extra.append(timeit.default_timer() - start)


# In[ ]:



