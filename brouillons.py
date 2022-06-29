#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Mar 27 19:29:27 2022

@author: root
"""
import math
import numpy
#Verifier si un nombre est premier ou pas
def testPrimeNumber(prime):
    tmp = 1
    racine = int(math.sqrt(prime))
    for i in range(2, (racine+1)):
        if(prime%i == 0):
            tmp = 0
            break
    return tmp
#La decomposition en produit de facteur premier d'un nombre
def DecompositionProduitFacteurPremier(nombre):
    Puissances = []
    while nombre!=0:
        d=2
        while nombre>1:
            while nombre%d ==0:
                nombre = nombre//d
                Puissances.append(d)
            d = d+1
        break
    return Puissances
#Fonction qui permet de recuperer un polynome de 
def polynome(r, p):
    print("Le degré du polynome est: ",r)
    print("Exemple: aX**2+bX+c avec a,b,c appartiennent a F",p)
    poly = input("Entrez un Polynome irreductible: ")
    print(poly)
#Representation des corps finis
corpZsurpZ = []
def corpsFinis(nombre):
    #si p est un nombre premier la representation du corps
    if testPrimeNumber(nombre) ==1:
        for i in range(nombre):
            corpZsurpZ.insert(i, i)
        print("################Le corps premier est :###########################")
        print('F',nombre," = ",corpZsurpZ)
    else:
        if len(numpy.unique(DecompositionProduitFacteurPremier(nombre))) == 1:
            print('ddd')
            print(DecompositionProduitFacteurPremier(nombre).count(2))
        else:
            print("La decomposition")
def log_element(x):
    j = 1
    for i in range(1, gf_ord):
        if Exp[i] == x%gf_card:
            j = i
            break
    return Log[Exp[j]]


def anti_log_element(index, poly_primitif):
    elemnt = index%gf_ord
    j = 0
    for i in range(len(Log)):
        if elemnt == Log[i]:
            j = i
            break
    return j
corpsFinis(16)
uni = len(numpy.unique(DecompositionProduitFacteurPremier(16)))
print(uni)
polynome(5, 2)
print(DecompositionProduitFacteurPremier(16))