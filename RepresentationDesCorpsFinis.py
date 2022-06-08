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
corpsFinis(16)
uni = len(numpy.unique(DecompositionProduitFacteurPremier(16)))
print(uni)
polynome(5, 2)
print(DecompositionProduitFacteurPremier(16))
##################################################################################"
    for i in range(nombre):
        conca = ""
        tab = FqBinai[i]
        temp = (len(tab)-1)
        for j in tab:
            if temp == 0:
                if j == str(1):
                    conca = conca + j
            elif j=="1" and len(tab)>=2:
                conca = conca + "X^" + str(temp) + "+"
            temp = temp -1
            if conca == "":
                conca = str(0)
        if conca[-1] == "+":
            conca = conca[:-1]
        FqPoly.append(conca)
    print("==============================Representation Polynomiale===================================")
    print('F'+str(nombre)+" = ",FqPoly)