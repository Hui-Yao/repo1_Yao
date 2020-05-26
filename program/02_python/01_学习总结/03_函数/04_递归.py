#!/usr/bin/env python
#-*- coding:utf-8 -*-
# Author = "Hui_Yao"

''''递归
1.定义：函数自身调用自身
2.要求：有明确的结束条件
       下一次递归的问题规模比上一次小
3.特点：python中最多递归999次，否则会导致栈溢出
       递归的效率较低
'''

#求5！
def calc(n):
    if n == 0:
        return 1    #结束条件：n == 0
    else:
        return n*calc(n-1)

print(calc(5))

'''
递归时，函数是由内向外逐层结束的，被调用函数运行时，调用函数停留在调用调用子函数的位置。

上题在求5！的运行情况大概如下：
1.将5传给calc，执行else下的子语句，虽然语句中包含return，但是由于调用了函数calc（4），没计算完，进入下一个循环，
calc（5）函数并未执行完，而是停留在计算clac（4）的过程中。
2.接下来计算clac（4），clac（3），calc（2），clac（1）的过程于上相同。
3.运行clac（0）时，执行if下的语句，返回数值1，其实这就是clac（0）的值。
4.将calc（0）返回调用者clac（1），此时calc（1）停留在 return n*calc(n-1)，
n = 1,clac(n-1) = clac(1-1) = clac(0) = 1,则n*calc(n-1) = 1，这也就是clac（1）的值
5.接着向上层返回数值，得到
calc(2) = n*calc(n-1) = 2*clac(1) = 2
calc(3) = n*calc(n-1) = 3*clac(2) = 6
calc(4) = n*calc(n-1) = 4*clac(3) = 24
calc(5) = n*calc(n-1) = 5*clac(4) = 120

至此，函数由内向外执行结束。


'''



