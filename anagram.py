# -*- coding: utf-8 -*-
"""
Created on Mon Nov 13 14:09:22 2017

@author: Vaidehee
"""

#check if the two words are anagram

def anagram(w1,w2):
    if (len(w1)!=len(w2)):
        print("not an angram")
    else:
        w1 = list(w1.lower())
        w2 = list(w2.lower())
        w1 = sorted(w1)
        w2 = sorted(w2)
        
        if (w1==w2):
            print("anagram")
        else:
            print("not an anagram")
        
w1=input("Enter a string")
w2=input("Enter another string")

anagram(w1,w2)