# -*- coding: utf-8 -*-
"""
Created on Mon Aug  3 17:30:50 2020

@author: user
"""


import random
thm = random.randint(1,10)
 
n = input("猜一個數字:")
n = int(n)
 
if thm == n:
    print("yes")
           
else:
    print("no")
          