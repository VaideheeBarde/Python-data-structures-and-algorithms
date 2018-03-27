# -*- coding: utf-8 -*-
"""
Created on Tue Mar 27 10:23:34 2018

@author: Vaidehee
"""

#we consider only non negative elements

#input
#finder([1,2,3,4,5,6,7], [2,3,4,5,6,1])

#output
#7

def finder(arr1, arr2):
    
    num = 0
    
    for n in arr1:
        num += n
        
    for n in arr2:
        num -= n
        
    return num
    
finder(arr1, arr2)
