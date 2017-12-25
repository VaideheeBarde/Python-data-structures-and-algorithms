# -*- coding: utf-8 -*-
"""
Created on Sun Dec 24 23:10:07 2017

@author: Vaidehee
"""

def countbits(num):
    import math
    i=1
    binary=0
    while(num>0):
        digit=num%2
        num=math.floor(num/2)
        binary=digit*i+binary
        i*=10
    return(binary)
    
num=int(input("Enter a number"))
print(countbits(num))