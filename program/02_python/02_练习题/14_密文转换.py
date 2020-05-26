#!/usr/bin/env python
#-*- coding:utf-8 -*-
# Author = "Hui_Yao"

secert = input('请输入密文：').upper().rstrip("END").strip('START')
# secert = input('请输入密文：').upper().strip('START')
len_input = len(secert)
source = list('ABCDEFGHIJKLMNOPQRSTUVWXYZ')

clear = []

for i in range(len_input):
    for j in source:
        if secert[i] == j:
            origin = source.index(j) - 5
            clear.append(source[origin])

print(clear)








