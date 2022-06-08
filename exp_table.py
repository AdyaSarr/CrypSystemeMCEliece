#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jun  7 13:00:32 2022

@author: root
"""
Exp = [1]
def exp_table(m, poly_primitif):
    for i in range((1<<m)-2):
        Exp.append(Exp[i]<<1)
    return Exp
print(exp_table(3, 11))

