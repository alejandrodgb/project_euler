#!/usr/bin/python

import pyprimes

#print max(pyprimes.factors(600851475143)) #easy way - pyprimes module

#written by myself
def split_in_digits(n):
    number_string, number_list=str(n), []
    for char in number_string:
        number_list.append(int(char))
    return number_list

def end_in_five(n):
    lt=split_in_digits(n)
    if lt[len(lt)-1]==5: return True
    else: return False

def is_prime(n):
    if n==2: return True
    if n%2==0: return False
    if sum(split_in_digits(n))%3==0: return False
    if end_in_five(n)==True: return False
    if n<2: return False
    iter=3
    while iter <= n**0.5:
        if n%iter==0: return False
        iter=iter+1
    return True

def largest_prime_factor(n):
    for i in range(n,0,-1):
        if n%i==0:
            if is_prime(i)==True:
                return True

print largest_prime_factor(600851475143)
