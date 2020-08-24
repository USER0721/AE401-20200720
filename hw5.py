# -*- coding: utf-8 -*-
"""
Created on Mon Aug 17 17:12:59 2020

@author: user
"""








scores = []
qaz = 0
edc = 0
wsx = 100
n = input('多少人?')
n = int (n)
for i in range (n):
    s = input('成績:')
    s = int(s)
    scores.append(s)
    qaz = qaz + s
for j in range(n):
    if scores[j] > edc:
        edc = scores[j]
        
    if scores[j] < wsx:
        wsx = scores[j]
print(scores)
print('總分是',qaz)
print('平均:',qaz/n)
print("最高是",edc)
print('最低是',wsx)
