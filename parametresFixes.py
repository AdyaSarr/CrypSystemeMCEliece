#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar 30 13:06:58 2022

@author: root
"""
import numpy as np
q = 16 #nombre d'element du corps F16
p = 2 #nombre d'element de F2
puissance = 4 #la puissance de p
primitif = [7, 11, 13, 19, 21, 25] #tableau de polynome

#La fonction de convertion binaire en polynome
def converBinaiPoly(nb):
    number = [] 
    for i in range(len(nb)):
        number.append(int(nb[i]))
    return np.poly1d(number, variable='X')