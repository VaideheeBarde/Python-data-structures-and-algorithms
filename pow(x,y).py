# -*- coding: utf-8 -*-
"""
Created on Tue Nov 21 00:32:15 2017

@author: Vaidehee
"""

#pow(x,y) -- pow(num,power)
#num=2 power=2 output=4
#num=5 power=5 output=3125
#num=12 power=12 output=24832

num=int(input("Enter a number to find its power"))
temp=num
power=int(input("Enter the power"))
i=1
while(i<power):
    i+=1
    num*=temp
print(temp, "raised to", power, "is", num)