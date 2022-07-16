#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jun 29 21:50:07 2022

@author: root
"""
import gf


gf.gf_init(gf.m)
#la multiplication de deux elements de Fq
def gf_multi(x, y):
    return gf.Exp[(gf.Log[x] + gf.Log[y])%gf.gf_ord]

#l'addition de deux elements de Fq
def gf_add(x, y):
    return x^y

#L'inverse d'un element de Fq
def gf_inv(x):
    return gf.Exp[gf.gf_ord - gf.Log[x]]

#la puissance d'un element de Fq
def gf_pow(x, p):
    return gf.Exp[(gf.Log[x]*p)%gf.gf_ord]

#la racine carré d'un element de Fq
def gf_sqrt(x):
    return gf.Exp[(gf.Log[x]<<gf.m-1)%gf.gf_ord]

#la division de deux elements de Fq
def gf_div(x, y):
    return gf_multi(x, gf_inv(y))

print("La multiplication des elements sont:")
print(gf_multi(4271, 7730))
print("L'addition des elements sont:")
print(gf_add(4271, 7730))
print("L'inverse d'un element est :")
print(gf_inv(4271))
print("La puissant de l'elements est:")
print(gf_pow(6347, 2))
print("La racine carrée est :")
print(gf_sqrt(7730))
print("La division des elements est:")
print(gf_div(7730, 4271))