# -*- coding: utf-8 -*-
"""
Created on Sat Nov 11 12:31:03 2017

@author: Vaidehee
"""


##segregate odd and even numbers
##output [5,3,7,9,4,6,2,8]
a=[4,5,6,3,2,7,8,9]
odd=[]
even=[]

for i in a:
    if(int(i%2)==1):
        odd.append(i)
    else:
        even.append(i)
        
print(odd+even)