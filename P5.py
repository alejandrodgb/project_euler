#!/usr/bin/python

def divisible(x,y):
    i=1
    while True:
        for n in range(x,y+1):
            if i%n==0:
                flag=True
            else: 
                flag=False
                break
        if i%100000==0: print i
        if flag==True: return i
        else: i+=1

print divisible(1,20)
