#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jun 23 09:50:16 2022

@author: root
"""
import parametresFixes
import tableAntiLog
import tableLog
def produit_2_element_Fq(element1, element2):
    return tableAntiLog.anti_log_element((tableLog.log_element(element1)+tableLog.log_element(element2))%(parametresFixes.q-1), parametresFixes.primitif[1])
