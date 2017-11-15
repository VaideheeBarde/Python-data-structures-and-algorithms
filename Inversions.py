# -*- coding: utf-8 -*-
"""
Created on Tue Nov 14 21:10:51 2017

@author: Vaidehee
"""

#Count the number of inversions in an array
#output-2

arr=[2,20,10,5,12]
l=len(arr)
count=0
for i in range(1,l):
    if(arr[i]<arr[i-1]):
        count+=1
print(count)