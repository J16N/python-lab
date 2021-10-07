# -*- coding: utf-8 -*-
"""
Created on Thu Sep 30 14:18:49 2021

@author: pc
"""

def is_prime(n):
   for i in range(2, n):
      if n % i == 0:
         return False
   return True

def twins_Prime(f,l):
   for i in range(f,l):
      j = i + 2
      if(is_prime(i) and is_prime(j)):
         print(i,"and",j,"are Twin primes")

n1= int(input("num one ::"))
n2 =int(input("num two ::"))
twins_Prime(n1, n2)