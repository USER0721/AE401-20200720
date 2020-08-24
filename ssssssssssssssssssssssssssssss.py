# -*- coding: utf-8 -*-
"""
Created on Mon Aug 24 16:34:25 2020

@author: user
"""


names=[]
scores=[]
total=0
n = input('人')
n = int(n)
for i in range(n):
    name = input('名:')
    names.append(name)
    score = input("分")
    score = int(score)
    scores.append(score)
for item in scores:
    total = total+item
print('平均:', (total/n))
highest=0
for i in range(n):
    if scores[i] > highest:
        highest = scores[i]
        highestname = names[i]
print(highestname, "最高分",highest)

lowest = 100
for i in range(n):
    if scores[i] < lowest:
        lowest = scores[i]
        lowestname = names[i]
print(lowestname, "最低分",lowest)










