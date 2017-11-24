# -*- coding: utf-8 -*-
"""
Created on Fri Nov 24 15:00:58 2017

@author: Vaidehee
"""

def find_century(year):
    century=int(year/100)
    arr=list()
    arr=[int(d) for d in str(year)]
    l=len(arr)
    if((arr[l-1] or arr[l-2])==0):
        print("The year", year, "belongs to", century, "century")
    else:
        century+=1
        print("The year", year, "belongs to", century, "century")
    
year=int(input("Enter a year to calculate the century it was from"))
find_century(year)