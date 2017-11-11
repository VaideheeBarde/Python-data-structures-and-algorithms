# -*- coding: utf-8 -*-
"""
Created on Sat Nov 11 12:31:03 2017

@author: Vaidehee
"""


####anagram
###input--
###Enter a string cinema
###Enter another string iceman
###output-- 
###It is an anagram
###This is case sensitive

new1=input("Enter a string")
new1=list(new1)
new1.sort()

new2=input("Enter another string")
new2=list(new2)
new2.sort()

if(new1==new2):
    print("It is an anagram")
else:
    print("Not an anagram")