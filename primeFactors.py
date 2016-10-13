# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

def isPrime(n):
    '''Checks if a number is prime'''
    if n == 2: return True
    if n == 3: return True
    if n % 2 == 0: return False
    if n % 3 == 0: return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i+2) == 0:
            return False
        i += i + 6
    return True



def primeFactors(n):
    '''Returns a list of prime factors for a number n'''
    results = []
    for i in range(int(n*0.5)+1):
        if i == 1: continue
        if isPrime(i):
            if n%i == 0:
                results.append(i)
    if len(results) == 0: results.append(n)
    return results
                

    