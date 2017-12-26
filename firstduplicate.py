# -*- coding: utf-8 -*-
"""
Created on Mon Dec 25 13:32:56 2017

@author: Vaidehee
"""

def firstduplicate(a):
    aset=set()
    
    for i in a:
        if i in aset:
            return i
        else:
            aset.add(i)
            
    if (len(aset)==len(a)):
        return -1
    else:
        return i
    
    
a=[1,2,3,1]           
print (firstduplicate(a))