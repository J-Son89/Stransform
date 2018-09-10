import numpy as np
import cmath
from scipy.linalg import hankel

##Functions
def SampleVector(Length, a,b, f):
    x = np.linspace(a,b,Length)
    return np.fromiter(map(f,x), dtype=complex)

def f(x):
    return sum([c*cmath.exp((xi) * (x)) for c,xi in zip(C,Xi)] )

def normalize(v): #used to normalise noise vector
    norm = np.linalg.norm(v)
    if norm == 0: 
       return v
    return v / norm

def vectToHankel(SV): #converts vect to Hankel
    return hankel(SV[0:N+1], SV[N:2*N+1])

#sets Hankel Basis Elements 
def basisToHankel(i):
    a = np.zeros(2*N+1,complex)
    a[i] = 1 
    return hankel(a[0:N+1], a[N:2*N+1])

N = 128

Rank = 8
gamma, sigma = 0, .5
a,b =-1,1

C =np.array([ 0.94737646+0.57831985j,  -0.93834136+0.80723275j,0.93370208-0.74539468j,  0.04446746-0.61503949j, 0.68611731+0.94646068j, -0.82304000+0.39125639j,0.233645-0.36850826j, -0.99867433+0.95581703j])
Xi = np.array([0.96607614 + 22.94274544j, 0.96607614-22.94274544j,-0.4+38.39425339j,  -0.4-38.39425339j,0.70902471+12.43801711j,  0.70902471-12.43801711j ,0+ 28.85837933j,  0-28.85837933j])

scale = 20

SV = SampleVector(2*N+1,a,b,f)
Fuzz = normalize( np.random.normal(gamma,sigma,2*N+1) )*scale  #generated noise & normalised
SVN= SV + Fuzz#F(x)

Hf= vectToHankel(SV) # noise free Hankel; F(x)-n(x)
HfN=vectToHankel(SVN); #Hankel with noise; F(x)

U,s,V = np.linalg.svd(HfN)
mu = ((s[Rank-1] +s[Rank] )**2/8)# set to square of mid-point of singular values 8 & 9


rho = 1.25 #(cmath.sqrt( 2*mu )/threshold) -1
#computes other component of HankelBasis so computation is only run once
HBNorm = np.array( [ basisToHankel(j)/(N+1 - abs(j-N)) for j in range( 2*N+1)],complex)