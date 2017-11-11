# -*- coding: utf-8 -*-
"""
Created on Sat Nov 11 12:31:03 2017

@author: Vaidehee
"""

#reverse a string

#input -
#Enter a word which you want to reverse - I am learning python

#output-
#nohtyp gninrael ma I

def revstring(arr,name,l):
    arr=arr[::-1]
    arr=''.join(arr)
    print(arr)

name = input("Enter a word which you want to reverse")
arr = list(name)
l=len(arr)
revstring(arr,name,l)