# -*- coding: utf-8 -*-
"""
Created on Sat Nov 18 17:23:10 2017

@author: Vaidehee
"""

#remove an element from an array
#input -8
#output - 5 1 2 3 7

a=[5,1,2,8,3,7]
print(a)
b=int(input(("Enter the element to be removed")))
m=0

for i in range (len(a)):
    if(a[i]!=b):
        a[m]=a[i]
        m=m+1
        
for k in range(m):
    print(a[k])