# -*- coding: utf-8 -*-
"""
Created on Mon Dec 25 11:21:47 2017

@author: Vaidehee
"""

arr=[5,6,4,2,3,2,-23]
oldprod=arr[0]*arr[1]
product=oldprod

if(len(arr)==2):
    product=oldprod
else:
    for i in range(2, len(arr)):
        newprod=arr[i]*arr[i-1]
        if(newprod>=oldprod):
            oparr=[]
            oparr.append(arr[i-1])
            oparr.append(arr[i])
            product=oparr[0]*oparr[1]
            oldprod=newprod
        
print(product)