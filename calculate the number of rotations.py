# -*- coding: utf-8 -*-
"""
Created on Sat Nov 11 12:31:03 2017

@author: Vaidehee
"""

#calculate the number of rotations in the array (elements should not be repeated)

#Enter the number of elements you want in the array 5
#Enter the elements
#element 1
#element 2
#element 3
#element 4
#element 5
#[1,2,3,4,5]
#Enter the rotated array
#element 3
#element 4
#element 5
#element 1
#element 2
#[3,4,5,1,2]

#output -
#Number of rotations are 3

def numOfRot(arr1,arr2,l):
    firstel=arr1[0]
    for i in range(0,l):
        if(arr2[i]-firstel==0):
            print("Number of rotations are",i)
        
arr1=list()
l=int(input("Enter the number of elements you want in the array"))
print("Enter the elements")
for i in range(0,l):
    num=int(input("element"))
    arr1.append(num)
print(arr1)
arr2=list()
print("Enter the rotated array")
for i in range(0,l):
    num=int(input("element"))
    arr2.append(num)
print(arr2)
numOfRot(arr1,arr2,l)