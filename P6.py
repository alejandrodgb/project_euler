#!/usr/bin/python

def sum_of_squares(start,end):
    n=0
    for i in range(start,end+1):
        n=n+(i+.0)**2
        if i%10==0: print i
    return n

def square_of_sum(start,end):
    n=0
    for i in range(start,end+1):
        n=n+(i+.0)
        if i%10==0: print i
    return n**2

def diff_sumsq_sqsum(start,end):
    sumofsquares = sum_of_squares(start,end)
    squareofsum = square_of_sum(start,end)
    return (squareofsum+.0)-sumofsquares

print diff_sumsq_sqsum(1,100)
