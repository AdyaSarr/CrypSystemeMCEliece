#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jun  7 13:00:32 2022

@author: root
"""
import parametresFixes
#table regroupant la representation exponentielle de chaque element de Fq
Exp = [0 for i in range((1<<parametresFixes.puissance))]
#la fonction exp_table retourne cette table
def exp_table(m, poly_primitif):
    Exp[0] = 1
    Exp[(1<<parametresFixes.puissance)-1]=Exp[0]
    for i in range(1, (1<<m)-1):
        Exp[i]=Exp[i-1]<<1
        if Exp[i]&(1<<m):
            Exp[i]^=poly_primitif
    return Exp
print(exp_table(parametresFixes.puissance, parametresFixes.primitif[1]))