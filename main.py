#Universidad del Valle de Guatemala
#Juan Pablo Pineda
#Hugo Román
#Laurelinda Gómez
#8/11/2021
#Lab 10

# -*- coding: utf-8 -*-
"""
Created on Tue Nov  9 20:24:54 2021

@author: hugo_
"""

import random
from math import pow

a=random.randint(2,10)

#To fing gcd of two numbers
def gcd(a,b):
    if a<b:
        return gcd(b,a)
    elif a%b==0:
        return b
    else:
        return gcd(b,a%b)

#For key generation i.e. large random number
def gen_key(q):
    key= random.randint(pow(10,20),q)
    while gcd(q,key)!=1:
        key=random.randint(pow(10,20),q)
    return key

def power(a,b,c):
    x=1
    y=a
    while b>0:
        if b%2==0:
            x=(x*y)%c;
        y=(y*y)%c
        b=int(b/2)
    return x%c

#For asymetric encryption
def encryption(msg,q,h,g):
    ct=[]
    k=gen_key(q)
    s=power(h,k,q)
    p=power(g,k,q)
    for i in range(0,len(msg)):
        ct.append(msg[i])
    # print("g^k used= ",p)
    # print("g^ak used= ",s)
    for i in range(0,len(ct)):
        ct[i]=s*ord(ct[i])
    return ct,p

#For decryption
def decryption(ct,p,key,q):
    pt=[]
    h=power(p,key,q)
    for i in range(0,len(ct)):
        pt.append(chr(int(ct[i]/h)))
    return pt


msg=input("Enter message:")

q=random.randint(pow(10,20),pow(10,50))
g=random.randint(2,q)
key=gen_key(q)
h=power(g,key,q)
# print("g used=",g)
# print("g^a used=",h)
ct,p=encryption(msg,q,h,g)
# print("Original Message=",msg)
# print("Encrypted Maessage=",ct)
pt=decryption(ct,p,key,q)
d_msg=''.join(pt)
# print("Decryted Message=",d_msg)

flag = True
while flag:
    option = input(
        "--------menu --------  \n1. Generar llaves. \n2. Cifrar \n3. Descifrar \n4. salir \n")
    
    if option == '1':
       
        print("**Llaves Generadas**")
        
        print("Public",g)
        print("Private",h)
        
    if option == '2':
        # msg = input("Ingrese el mensaje a cifrar: ")
        
        print("***El mensaje ha sido cifrado***")
        print("Encrypted Maessage=",ct)
        
    if option == '3':
        print("***El mensaje ha sido descifrado***")

        print("Decryted Message=",d_msg)

       
    if option == '4':
        flag = False
        
    
    
