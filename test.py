#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar 30 21:36:21 2022

@author: root
"""

m=3
poly_prim=11
card=1<<m #card=2^m
Exp=[0 for i in range(card)] #permet d'initialiser la liste a 0
Log_table=[0 for i in range(card)]
def exp_table():
    Exp[0]=1
    Exp[card-1]=1
    for i in range(1,card-1):
        Exp[i]=Exp[i-1]<<1 # Exp[i]=2*Exp[i-1] ou a^n=a*a^(n-1)
        if(Exp[i]&(1<<m)):
            Exp[i]^=poly_prim # ^ represente le XOR
    return Exp

print(exp_table())


def log_table():
    exp_table()
    Log_table[0]=-1
    for i in range(1,card-1):
        Log_table[Exp[i]]=i
    return Log_table

print(log_table())