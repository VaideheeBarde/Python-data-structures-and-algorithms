# -*- coding: utf-8 -*-
"""
Created on Tue Mar 27 17:40:06 2018

@author: Vaidehee
"""

#input=[1,2,3,4] output=10
#input=[1,2,-1,3,4,10,10,-10,-1] output=29
#input=[-1,1] output=1


def max_continuous_sum(arr):
    
    if len(arr) == 0:
        return 0
    
    elif len(arr) == 1:
        return arr[0]
    
    max_sum = total = arr[0]
        
    for n in arr[1:]:
        total = max(total+n, n)
        max_sum = max(max_sum, total)
        
    return max_sum

max_continuous_sum(arr)

