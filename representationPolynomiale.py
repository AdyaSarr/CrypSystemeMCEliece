#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar 30 21:36:21 2022

@author: root
"""

import parametresFixes
Fq = []#table pour la representation decimale
FqPoly = []#table pour la representation polynomiale
FqBinai = []#table pour la representation binaire

#La fonction qui permet de donner la representation polynomiale de chaque element de Fq
def corpsFinisPolynome(nombre, premier, puiss):
    print("F"+str(nombre)+"=F"+str(premier)+"[X]/<P(X)>")#Ecriture du corps
    print("Le polynome quotient P(x) est:")
    #le polynome quotient
    print(parametresFixes.converBinaiPoly("{0:b}".format(parametresFixes.primitif[2])))
    print("F"+str(nombre)+"={q(X) ∈ F"+str(premier)+" telle que dq<"+str(puiss)+"}")
    for i in range(nombre):
        Fq.append(i)
    print('F'+str(nombre)+" = ",Fq)
    for i in range(nombre):
        FqBinai.append("{0:b}".format(Fq[i]))
        FqPoly.append(parametresFixes.converBinaiPoly(FqBinai[i]))
    return FqPoly
print(corpsFinisPolynome(parametresFixes.q, parametresFixes.p, parametresFixes.puissance)[15])



