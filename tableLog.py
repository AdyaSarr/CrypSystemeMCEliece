#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jun  9 17:55:13 2022

@author: root
"""
import parametresFixes#on importe le fichier parametresFixes qui contient toutes les constantes du code
import representationExponentielle#nous avons importer le fichier qui permet de donner la representation exponentielle des element de Fq

Log = [0 for i in range((1<<parametresFixes.puissance))]
def log_table(m):
    Log[0]=-1
    for i in range(1,(1<<m)-1):
        Log[representationExponentielle.Exp[i]]=i
    return Log
def log_element(x):
    j = 1
    for i in range(1, (1<<parametresFixes.puissance)-1):
        if representationExponentielle.Exp[i] == x%parametresFixes.q:
            j = i
            break
    return Log[representationExponentielle.Exp[j]]
print(log_table(parametresFixes.puissance))
print(log_element(7))