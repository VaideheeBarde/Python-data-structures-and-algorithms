# -*- coding: utf-8 -*-
"""
Created on Tue Jan 23 23:42:40 2018

@author: Vaidehee
"""

#replace all 0's in an input integer with 5's

#input - 2017  output - 2517
#input - 000  output - 555
#input - 255  output - 255

a=(input("Enter a number"))

arr=list()
for x in (a):
    arr.append(int(x))

newarr=list()
for x in arr:
    if x==0:
        newarr.append(5)
    else:
        newarr.append(x)
        
number="".join(map(str,newarr))
print(number)