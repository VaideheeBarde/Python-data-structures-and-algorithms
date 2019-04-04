# -*- coding: utf-8 -*-
"""
Created on Mon Nov 13 14:58:27 2017

@author: Vaidehee
"""

#bubble-sort

#input - Your array [6,2,8,1]
#output - Array after performing the bubble sort [1,2,6,8]

def bubble_sort(a,l):
#Traversing through the entire array
    for j in range(l):
#Keeping the last element (largest) in last place and rearranging the initial array
        for i in range(0,l-1-j):
            if(a[i]>a[i+1]):
                temp=a[i]
                a[i]=a[i+1]
                a[i+1]=temp
    print("Array after performing the bubble sort",a)

a = list()
l= int(input("Number of elements in the array"))
print("Enter elements")
for i in range(l):
    element=int(input("Enter element:"))
    a.append(element)
print("Your array",a)
bubble_sort(a,l)
