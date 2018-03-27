# -*- coding: utf-8 -*-
"""
Created on Mon Mar 26 20:24:37 2018

@author: Vaidehee
"""


# input 
# arr=[1,2,3,4] k=5
# output -
# {(2,3),(1,4)}

#input
#arr = [1,2,3] k=3
#output -
# {(1,2)}


def pair_array(arr, k):
    
    seen=set()
    output=set()
    
    for num in arr:
        target = k-num
        if target not in seen:
            seen.add(num)
        else:
            output.add((min(target,num), max(target,num)))
            
    print(output)

arr=[1,2,3,4]
k=5    
pair_array(arr, k)