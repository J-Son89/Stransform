#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import numpy as np
import cmath
"""
Created on Thu Sep  6 12:15:11 2018

@author: jamie
"""

def h(xj,x): # function in least squares to form matrix A
    return np.array([ (cmath.exp((xj[j]) * (x))) for j in range(len(xj)) ],complex)

def getConstants(XI,vect,a,b): #least squares
    x = np.linspace(a,b,len(vect))
    A= np.array([h( XI,xi) for xi in x ],complex )
    return np.linalg.lstsq(A,vect,rcond=-1)[0]