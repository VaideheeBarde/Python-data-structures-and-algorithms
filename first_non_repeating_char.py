# -*- coding: utf-8 -*-
"""
Created on Wed Nov 15 00:27:03 2017

@author: Vaidehee
"""

#first non-repeating character in a string
#output= H

def count_char(string):
    count=[0]*256
    for i in string:
        count[ord(i)]+=1
    return count

def first_non_repeat_char(string):
    count=count_char(string)
    for i in string:
        if (count[ord(i)]==1):
            print(i)
            break
    pass

first_non_repeat_char("Hello")