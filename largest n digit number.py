# -*- coding: utf-8 -*-
"""
Created on Sat Nov 25 17:14:44 2017

@author: Vaidehee
"""

#largest n digit num
#input - 2 output - 99
#input - 7 output -9999999
#input - 1 output - 9

def largest_num(n):
    num=1
    rem=0
    for i in range(n):
        rem=9*num+rem
        num*=10
    return rem

n=int(input("Enter the value of n"))
print("The largest", n, "digit number is", largest_num(n))