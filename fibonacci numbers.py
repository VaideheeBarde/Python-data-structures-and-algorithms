# -*- coding: utf-8 -*-
"""
Created on Mon Dec 25 00:52:31 2017

@author: Vaidehee
"""


#print an array of fibonacci numbers

n=int(input("Enter a number"))
arr=[1,1]

for i in range(2,n):
    digit=arr[i-1]+arr[i-2]
    arr.append(digit)
    
print(arr)