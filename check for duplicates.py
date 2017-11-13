# -*- coding: utf-8 -*-
"""
Created on Mon Nov 13 15:27:50 2017

@author: Vaidehee
"""

#check if there are duplicate present in the list
#input [1,2,2]
#output - duplicates present

#input [1,2,3]
#output - no duplicates

def duplicates(a,l):
    b=set(a)
    if(len(a)>len(b)):
        print("duplicates present")
    else:
        print("no duplicates")
        
a=list()
l=int(input("Enter the number of elements in the array"))
for i in range(l):
    element=int(input("Enter element: "))
    a.append(element)
    
duplicates(a,l)