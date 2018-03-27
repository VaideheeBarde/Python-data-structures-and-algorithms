# -*- coding: utf-8 -*-
"""
Created on Mon Mar 26 18:11:46 2018

@author: Vaidehee
"""

def arrSumPairs(arr,k):
    
    counter = 0
    lookup = set()
    
    for num in arr:
        if (k-num) in lookup:
            counter+=1
        else:
            lookup.add(num)
            
    print(counter)
    
arrSumPairs([1,2,3,4], 5)
arrSumPairs([1,2,3,3], 3)
arrSumPairs([3,4,5,6], 9)
arrSumPairs([1,3,2,2], 4)