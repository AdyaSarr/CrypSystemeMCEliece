#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jun  9 17:55:34 2022

@author: root
"""
import parametresFixes
import representationExponentielle

AntiLog = representationExponentielle.Exp

def anti_log_element(index, poly_primitif):
    elemnt = 1<<index
    print(elemnt)
    j = 0
    for i in range(1, (1<<parametresFixes.puissance)-1):
        if AntiLog[i] == elemnt:
            j = i
            break
    return AntiLog[j]
print(anti_log_element(6, parametresFixes.primitif[1]))