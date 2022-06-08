#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar 30 21:36:21 2022

@author: root
"""
import numpy as np

number = []
nb = "{0:b}".format(11)
for i in range(len(nb)):
    number.append(int(nb[i]))
print(np.poly1d(number))
print(type(number))