#!/usr/bin/python

def multiples(n):
    numbers_list, x  = [], 0
    for number in range(n):
        if number%5==0 or number%3==0:
            numbers_list.append(number)
    for each in numbers_list:
        x = x + each
    return x

print(multiples(1000))
