# -*- coding: utf-8 -*-
"""
Created on Sat Nov 11 14:41:08 2017

@author: Vaidehee
"""

#segregate even and odd numbers
def evenodd(a,l):
    even=[]
    odd=[]
    for i in range(0,l):
        if(a[i]%2==0):
            even.append(a[i])
        
        else:
            odd.append(a[i])
        
    a=even+odd
    print(a)

a=list()
l=int(input("Enter the number of elements"))
print("Enter all the elements")
for i in range(0,l):
    element=int(input("Enter element"))
    a.append(element)
print(a)
evenodd(a,l)