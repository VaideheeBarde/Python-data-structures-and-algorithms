# -*- coding: utf-8 -*-
"""
Created on Mon Mar 26 10:20:43 2018

@author: Vaidehee
"""

def anagram(a,b):
    a=a.replace(" ","").lower()
    b=b.replace(" ","").lower()
    
    if(len(a)!=len(b)):
        return False
    
    counter={}
    
    for letter in a:
        if letter in counter:
            counter[letter]+=1
        else:
            counter[letter]=1
            
    for letter in b:
        if letter in counter:
            counter[letter]-=1
        else:
            counter[letter]=1
        
    for k in counter:
        if counter[k]!=0:
            return False
    return True
    pass

anagram("clint eastwood", "old west action")
