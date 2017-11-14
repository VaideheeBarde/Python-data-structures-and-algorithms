# -*- coding: utf-8 -*-
"""
Created on Mon Nov 13 17:29:51 2017

@author: Vaidehee
"""

#factorial of a number

#input = 0 output = 1
#input = 1 output = 1
#input = 10 output =3628800

def factorial(num):
    fact=1
    if(num==0):
        print("The factorial of", num, "is", fact)
    else:
        for i in range(1,num+1):
            fact*=i
    print("The factorial of", num, "is", fact)
    
num=int(input("Enter a number to calculate its factorial"))
factorial(num)