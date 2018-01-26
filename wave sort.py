# -*- coding: utf-8 -*-
"""
Created on Fri Jan 26 01:51:25 2018

@author: Vaidehee
"""

def waveSort(arr,l):
    arr.sort()
    
    for i in range(0,l-1,2):
        arr[i],arr[i+1]=arr[i+1],arr[i]
        
    print(arr)
    
l=int(input("Enter the number of elements in an array"))
print("Enter the array")
arr=list()
for i in range (0,l):
    n=int(input("Enter the number"))
    arr.append(n)
print(arr)
waveSort(arr,l)