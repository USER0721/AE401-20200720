# -*- coding: utf-8 -*-
"""
Created on Mon Aug 24 17:38:51 2020

@author: user
"""



scores=[]
total=0
n = input('人')
n = int(n)
for i in range(n):
    name = input('名:')
    scores.append(name)
    score = input("分")
    score = int(score)
    scores.append(score)
for item in range(1,n*2,2):
    total = total+scores[item]
print('平均:', (total/n))
highest=0
for i in range(1,n*2,2):
    if scores[i] > highest:
        highest = scores[i]
        highestname = scores[i-1]
print(highestname, "最高分",highest)

lowest = 100
for i in range(1,n*2,2):
    if scores[i] < lowest:
        lowest = scores[i]
        lowestname = scores[i-1]
print(lowestname, "最低分",lowest)