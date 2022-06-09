#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar 30 13:06:58 2022

@author: root
"""
import sympy as sp
q = 16 #nombre d'element du corps F16
p = 2 #nombre d'element de F2
puissance = 4 #la puissance de p
primitif = [7, 11, 13, 19, 21, 25] #tableau de polynome 
#La fonction de convertion binaire en polynome
def converBinaiPoly(bits):
    for i in range(len(bits)):
        conca = ""
        temp = (len(bits)-1)
        for j in bits:
            if temp == 0:
                if j == str(1):
                    conca = conca + j
                
            elif j=="1" and len(bits)>=2:
                conca = conca + "X^" + str(temp) + "+"
            temp = temp -1
            if conca == "":
                conca = str(0)
        if conca[-1] == "+":
            conca = conca[:-1]
    return conca