# -*- coding: utf-8 -*-
"""
Created on Sat Nov 11 12:31:03 2017

@author: Vaidehee
"""

#sum of multiplication of every element with its index

#input -
#Enter the number of elements in the array 5
#Enter all the elements
#Element: 8
#Element: 4
#Element: 5
#Element: 2
#Element: 3
#[8,4,5,2,3]

#output -
#The sum of multiplication of each array element with its index is 32

def find_total(arr,l):
    total=0
    mul=0
    for i in range(0,l):
        mul=i*arr[i]
        total=total+mul
    print("The sum of multiplication of each array element with its index is",total)

arr=list()
l=int(input("Enter the number of elements in the array"))
print("Enter all the elements")
for i in range(0,l):
    element=int(input("Element:"))
    arr.append(element)
print(arr)
l=int(len(arr))
find_total(arr,l)