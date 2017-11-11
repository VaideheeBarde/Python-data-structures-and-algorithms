# -*- coding: utf-8 -*-
"""
Created on Sat Nov 11 14:41:08 2017

@author: Vaidehee
"""

#sorting a list of 0s and 1s using direct method
aList =[0,1,0,1,1,0,0]
aList.sort()
print(aList)

#sorting a list of 0s and 1s using the traditional method
a=[0,1,0,1,1,0,0]
l=len(a)
count=0
for i in range(0,l):
    if(a[i]==0):
        count+=1 #counting the number of zeros in the array 
for i in range(0,count):
    a[i]=0 #printing all the zeros in the array at the beginning      
for i in range(count,l):
    a[i]=1 #printing all the ones in the array after the count of zeros  
print(a)