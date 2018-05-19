#!/usr/bin/python

def multiples(n):
    numbers_list, x  = [], 0
    for number in range(n):
        #print "num: %d, mod 5: %d" % (number, number%5)
        #print "num: %d, mod 3: %d" % (number, number%3)
        if number%5==0 or number%3==0:
            numbers_list.append(number)
    for each in numbers_list:
        x = x + each
    return x

print multiples(1000) 
