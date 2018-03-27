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

#############################__method1__#################################

def finder1(arr1, arr2):
    
    num = 0
    
    for n in arr1:
        num += n
        
    for n in arr2:
        num -= n
        
    return num
    
finder1(arr1, arr2)


###########################__method2__##################################

def finder2(arr1, arr2):
    
    arr1.sort()
    arr2.sort()
    
    for num1, num2 in zip(arr1, arr2):
        if num1!=num2:
            return num1
    
    return arr1[-1]

finder2(arr1, arr2)


##########################__method3__####################################

import collections

def finder3(arr1, arr2):
    
    d=collections.defaultdict(int)
    
    for num in arr2:
        d[num] += 1
        
    for num in arr1:
        if d[num] == 0:
            print(num)
        else:
            d[num] -= 1
            
finder3([5,5,7,7], [5,5,7])

