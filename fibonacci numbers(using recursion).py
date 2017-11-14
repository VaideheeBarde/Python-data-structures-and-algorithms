# -*- coding: utf-8 -*-
"""
Created on Tue Nov 14 00:35:41 2017

@author: Vaidehee
"""

#program for fibonacci numbers using recursion
#input n=9
#output n=34

def fib(n):
    if(n<0):
        print("Cannot find fibonacci")
    elif(n==0 or n==1):
        return n
    else:
        return(fib(n-1)+fib(n-2))
        
n=int(input("Enter a number to calculate the fibonacci number:"))
print(fib(n))