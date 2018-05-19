#!/usr/bin/python
import time


def fib(n):
    fib_list=[]
    a, b  = 0, 1 
    while a<=n:
        fib_list.append(a)
        a,b=b,a+b
    return fib_list

def sum_even_fib(n):
    fib(n)
    sum=0
    for i in fib_list:
        sum=sum+i
    return sum

print fib(5)
