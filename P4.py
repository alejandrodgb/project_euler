#!/usr/bin/python

def simetric(n):
    n=str(n)
    if n[0:len(n)/2]==n[len(n)/2:len(n)][::-1]:
        return True
    return False

def palindromes_list(max,min):
    palindromes=[]
    for i in range(max*max,min*min,-1):
        if simetric(i)==True:
            palindromes.append(i)
    return palindromes

def palindrome_factors(max,min,digits):
    palindrome_list=palindromes_list(max,min)
    for each_palindrome in palindrome_list:
        for i in range(max,min,-1):
            number=each_palindrome/(i+.0)
            if str(number)[digits:]=='.0':
                return each_palindrome, number, i
    return 'None Found'
            
print palindrome_factors(999,100,3)
