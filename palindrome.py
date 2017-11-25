# -*- coding: utf-8 -*-
"""
Created on Mon Nov 20 23:03:25 2017

@author: Vaidehee
"""

#palindrome number

#input - 121 output - palindrome
#input - 12321 output - palindrome
#input - 1234 output - not a palindrome
#input - -121 output - not a palindrome(since it is a negative number)

import math
num=int(input("Enter a number to find if it's a palindrome"))
n=num
reverse=0

while(num>0):
    digit=num%10
    reverse=reverse*10+digit
    num=math.floor(num/10) #we need to floor down the integer here
    
if(reverse==n):
    print("Voila! It is a palindrome")
else:
    print("Alas! It is not a palindrome")
