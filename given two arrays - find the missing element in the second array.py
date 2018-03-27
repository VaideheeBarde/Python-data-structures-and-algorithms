# -*- coding: utf-8 -*-
"""
Created on Tue Mar 27 10:23:34 2018

@author: Vaidehee
"""


def finder(arr1, arr2):
    
    num = 0
    
    for n in arr1:
        num += n
        
    for n in arr2:
        num -= n
        
    return num
    
finder(arr1, arr2)