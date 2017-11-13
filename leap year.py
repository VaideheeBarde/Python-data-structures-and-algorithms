# -*- coding: utf-8 -*-
"""
Created on Mon Nov 13 14:09:22 2017

@author: Vaidehee
"""

#find leap year
year = int(input("Enter a year"))
if(year%400==0 or year%100==0 or year%4==0):
    print("Leap year")
else:
    print("Not a leap year")