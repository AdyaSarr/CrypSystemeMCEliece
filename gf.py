# -*- coding: utf-8 -*-

import parametres as para

primitive_polynomials = [1, 3, 7, 11, 19, 37, 67, 131, 285, 545, 1033, 2053, 4179, 8219]
m = para.ext_degre
poly_primitif = primitive_polynomials[m]
gf_card = para.gf_cardinalyte
gf_ord = para.gf_order

Exp = [0 for i in range(gf_card)]
Log = [0 for i in range((gf_card))]

#fonction pour la representation exponentielle des elements de Fq
def exp_table(m, poly_primitif):
    Exp[0] = 1
    Exp[gf_ord]=1
    for i in range(1, gf_ord):
        Exp[i]=Exp[i-1]<<1
        if Exp[i]&gf_card:
            Exp[i]^=poly_primitif
    return Exp
#table pour la puissance de chaque element de Fq
def log_table(m):
    Log[0]='existe_pas'
    for i in range(1, gf_ord):
        Log[Exp[i]]=i
    return Log

def gf_init(m):
    log_table(m)
    exp_table(m, poly_primitif)
gf_init(m)

print("La representation exponentielle est:")
print(exp_table(m, poly_primitif))
print("===========================================================================================")
print("la table log est")
print(log_table(m))