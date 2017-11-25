# -*- coding: utf-8 -*-
"""
Created on Sat Nov 25 09:53:43 2017

@author: Vaidehee
"""

#find the first duplicate

def first_duplicate(a):
    l=len(a)
    uniq=[]
    dup=[]
    if(a!=list(set(a))):
        for i in range(l):
            if(a[i] not in uniq):
                uniq.append(a[i])
            else:
                dup.append(a[i])
                break
        print("The first duplicate is", sum(dup))
    else:
        print("No duplicates")

l=int(input("Enter the length of the array"))
print("Enter the array")
a=list()
for i in range(l):
    element=int(input("Enter the element"))
    a.append(element)
print(a)
first_duplicate(a)