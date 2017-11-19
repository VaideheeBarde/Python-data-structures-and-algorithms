# -*- coding: utf-8 -*-
"""
Created on Sun Nov 19 13:04:17 2017

@author: Vaidehee
"""

#reverse a number - easy method

#input - 356
#output - 653

#input - 5963
#output - 3695

def reverse_a_num(num):
    a=list(str(num))
    a=a[::-1]
    a=''.join(a)
    print(a)

num=int(input("Enter a number"))
reverse_a_num(num)