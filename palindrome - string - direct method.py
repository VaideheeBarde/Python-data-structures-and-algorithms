# -*- coding: utf-8 -*-
"""
Created on Tue Nov 28 23:50:53 2017

@author: Vaidehee
"""

#palindrome - string - direct method

#input - radar output - palindrome
#input - abc output - not a palindrome
#input - v output - palindrome

def palindrome(word):
    new_word=word[::-1]
    if(word==new_word):
        print("It is a palindrome")
    else:
        print("It is not a palindrome")
        
word=input("Enter a word to find if it is a palindrome")
palindrome(word)