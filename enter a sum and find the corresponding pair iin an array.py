# -*- coding: utf-8 -*-
"""
Created on Sat Nov 11 12:31:03 2017

@author: Vaidehee
"""

#In a sorted and rotated array, find if there is a pair with a given sum

#input -
#Enter number of elements in the array 3
#Enter the array
#Element: 1
#Element: 2
#Element:3

#output -
#[1,2,3]

#input -
#Enter a sum to find the corressponding pair 4
#Sum with 3 and 1

def find_sum(arr,l,num):
    for j in range(0,l):
        for i in range(j+1,l):
            if(arr[j]+arr[i]==num):
                print ("Sum with %r and %r" %(arr[i],arr[j]))

arr=list()            
l=int(input("Enter number of elements in the array"))
print("Enter the array")
for i in range(l):
    element=int(input("Element:"))
    arr.append(element)
print(arr)
num=int(input("Enter a sum to find the corressponding pair"))
find_sum(arr,l,num)