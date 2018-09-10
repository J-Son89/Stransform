import numpy as np
import config
#import prof
#profile = prof.profile 
rho = config.rho
mu = config.mu
N = config.N

HBNorm = config.HBNorm # compute HB[j]/(N+1 - abs(j-N) in config

def ADMM(X,Y,Lambda,Hf):
    X = Xupdate((Hf - Lambda + (rho*Y) )/(1+rho)) #input is D_1
    Y = Yupdate(X + Lambda/rho) #input is D_2
    Lambda = Lambda + rho*(X-Y)
    return X,Y,Lambda

def Xupdate(D):
    U,s,V = np.linalg.svd(D)
    singularV = np.fromiter(map(argminT,s),complex)
    return np.matmul((U * [singularV]), V)

def argminT(d):
    if( abs(d)>= 0 and abs(d) < (np.sqrt(2*mu))/(1+rho)):
        return 0
    elif( abs(d) >= (np.sqrt(2*mu))/(1+rho) and abs(d) < np.sqrt(2*mu) ):
        return (d*(1+rho))/ (rho) - (np.sqrt(2*mu))/rho
    else:
        return d

def Yupdate(D): #takes trace of D* HBj (jth HankelBasis elements) * HBj/ tj, where tj is the appropriate norm
    D = D[:, ::-1]
    Y=0
    for i in range(2*N+1):
        Y = Y + np.sum(np.diag(D, N-i) )* HBNorm[i]
    return Y