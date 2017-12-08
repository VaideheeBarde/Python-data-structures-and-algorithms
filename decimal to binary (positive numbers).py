# -*- coding: utf-8 -*-
"""
Created on Thu Dec  7 20:58:29 2017

@author: Vaidehee
"""

#decimal to binary

#input - 0 output - 0
#input - 37 output - 100101
#input - 1 output - 1

def dectobin(num):
    import math
    i=1
    binary=0
    while(num>0):
        digit=num%2
        num=math.floor(num/2)
        binary+=digit*i
        i*=10
    print(binary)
    
num=int(input("Enter a number"))
dectobin(num)