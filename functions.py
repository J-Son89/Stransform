#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import numpy as np
from scipy.linalg import hankel
import cmath

"""
Created on Thu Sep  6 12:19:34 2018

@author: jamie
"""

def g(x,XI,CI):
    return sum([c*cmath.exp((xi) * (x)) for c,xi in zip(CI,XI)] )

def ApproxVector(Length,L,R,XI,CI): 
    x = np.linspace(L,R,Length)
    return np.array([g(xi,XI,CI) for  xi in x], complex)    
    
def avgAD(Hf,N,i): #takes the average of anti-diagonal values
    antidiagonal = np.diag(Hf, N-i)
    return np.sum(antidiagonal)/ len(antidiagonal)
    
def hankelToVect(Hf,N): #converts a Hankel to a vector of averaged anti-diagonal values
    return np.array([ avgAD(Hf,N,i) for i in range(2*N+1)],complex)

def vectToHankel(SV,N): #converts vect to Hankel
    return hankel(SV[0:N+1], SV[N:2*N+1])