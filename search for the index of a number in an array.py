# -*- coding: utf-8 -*-
"""
Created on Sat Nov 11 12:31:03 2017

@author: Vaidehee
"""

#find the index of an element in a sorted and a rotated array

#input -
#How many elements 3
#element:5
#element:8
#element:9
#Enter the number whose index you want to find 8

#output -
#found at index 1

def find_el(arr,num,element):
    for i in range(0,element):
        if (arr[i]==num):
            print("found at index",i)
            
arr=list()
element=int(input("How many elements"))
print("Enter numbers")
for i in range(element):
    d=input("element:")
    arr.append(int(d))
num = int(input("Enter the number whose index you want to find"))
find_el(arr,num,element)