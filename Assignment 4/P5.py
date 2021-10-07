# -*- coding: utf-8 -*-
"""
Created on Thu Sep 30 14:28:36 2021

@author: pc
"""

def Palin(n):
    temp=n
    rev=0
    while(n>0):
        dig=n%10
        rev=rev*10+dig
        n=n//10
    if temp == rev:
        return True
    else:
        return False


def Prime(n):
    
    if n == 1:
        return False
   
    for i in range(2,n):
        if n % i == 0:
            return False
    
    return True


n=int(input("Enter the 1st number  : "))
n2=int(input("Enter the 2nd number  : "))
print("The prime palindromes in this range are : ")
for i in range(n, n2+1):
    if Palin(i) and Prime(i):
        print(i,end=" ")
        
    
    
    
    
    
    
    
    
    
    
    