# -*- coding: utf-8 -*-
"""
Created on Fri Nov 20 17:23:14 2015
 
@author: Philipp
"""
 
 
a = 5
b = 9
N = 10
k = 0
#f = x**3
c = 0
s = 0.000000
h = 0.000000
 
def f(x):
    return (x**3)
     
if N%2!=0:
    print ("N muss gerade sein!")
else:
    h = (b-a)/N
    x = a+k*h
    s = f(x)
    for k in range (int (N/2-1)):
        c = c + f(a+2*k*h)
        k = k+1
    s = s + 2*c
    k = 1
    c = 0
    for k in range (int (N/2)):
        c = c + f(a+ (2*k-1)*h)
        k = k+1
    s = s + 4*c
    s = s + f(a + N*h)
    print ("Ergebnis= ", s)