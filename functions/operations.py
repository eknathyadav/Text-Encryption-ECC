# -*- coding: utf-8 -*-
"""
Created on Mon Sep  7 21:59:12 2020

@author: Eknath
"""
def txt2ascii(st):     # converts text to ascii
    ascii_string = []
    for i in st:
        ascii_string.append(ord(i))
    return ascii_string
def toDigits(n, b):
    """Convert a positive number n to its digit representation in base b."""
    digits = []
    while n > 0:
        digits.insert(0, n % b)
        n  = n // b
    #return int(''.join(map(str,digits)))
    return digits
def grouping(list,pairn): #It will partition the ascii values into groups
    groupsList,n,l = [],0,[]
    for i in range(len(list)):
        l.append(list[i])
        n = n+1
        if n==pairn :
            groupsList.append(l)
            n,l = 0,[]
        elif i==len(list)-1:
            groupsList.append(l)
    return groupsList
def fromDigits(digits, b):
    """Compute the number given by digits in base b."""
    n = 0
    for d in digits:
        n = b * n + d
    return n
def bigInteger(list): #converts each group of ascii value into big Integer.
    bigI = []
    for i in list:
        bigI.append(fromDigits(i,65536))
    if len(bigI)%2!=0:
        bigI.append(32)
    return bigI
