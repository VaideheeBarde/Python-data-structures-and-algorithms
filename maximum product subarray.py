# -*- coding: utf-8 -*-
"""
Created on Sat Nov 11 14:41:08 2017

@author: Vaidehee
"""

#maximum product subarray

#Here the 3 consecutive elements 1,7,8 five the highest product in comparison to the other consecutive numbers

arr=[-2,-3,1,7,8,0,5]
n=len(arr)
max_ending_here=1
min_ending_here=1
max_so_far=1

for i in range(0,n):
    if(arr[i]>0):
        max_ending_here=max_ending_here*arr[i]
        min_ending_here=min(min_ending_here*arr[i],1)
    elif(arr[i]==0):
        max_ending_here=1
        min_ending_here=1
    else:
        temp=max_ending_here
        max_ending_here=max(min_ending_here*arr[i],1)
    if(max_so_far<max_ending_here):
        max_so_far=max_ending_here
print(max_so_far)