#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jun  9 17:55:34 2022

@author: root
"""
import parametresFixes
import tableLog

def anti_log_element(index, poly_primitif):
    elemnt = index%(parametresFixes.q - 1)
    j = 0
    for i in range(len(tableLog.Log)):
        if elemnt == tableLog.Log[i]:
            j = i
            break
    return j
print(anti_log_element(7, parametresFixes.primitif[1]))