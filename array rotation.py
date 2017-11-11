# -*- coding: utf-8 -*-
"""
Created on Sat Nov 11 12:31:03 2017

@author: Vaidehee
"""

#array rotation by right
#input 123456
#output 612345
a=input("Enter an array")
d=int(input("Enter by how much you want to rotate"))
print(a[-d:]+a[:-d])

#array rotation by left
#input 123456
#output 234561
a=input("Enter an array")
d=int(input("Enter by how much you want to rotate"))
print(a[d:]+a[:d])