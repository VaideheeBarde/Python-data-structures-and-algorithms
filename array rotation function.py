# -*- coding: utf-8 -*-
"""
Created on Sat Nov 11 12:31:03 2017

@author: Vaidehee
"""

#array rotation algorithm - left
#output [3,4,5,1,2]
def arr_rotate(arr,d,n):
    while(d>0):
        for i in range(0,n-1):
            temp=arr[i]
            arr[i]=arr[i+1]
            arr[i+1]=temp
        d-=1
    return arr
    
arr=[1,2,3,4,5]
n=len(arr)
d=int(2)
print(arr_rotate(arr,d,n))