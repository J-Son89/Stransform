import numpy as np
import cmath
import config

def Esprit(X):
    U,s,V = np.linalg.svd(X)
    U = U[:,:config.Rank]
    Uplus = np.delete(U, (0), axis=0) # sets U+ by removing first row of U
    Uminus = np.delete(U, (int((U.shape[0])-1)), axis=0) # sets U- by removing last row of U
    UminusConTrans= np.conj(Uminus).transpose() # U^*
    FactorOne = np.linalg.inv( np.matmul( UminusConTrans,Uminus )) #(u^* times U- )^-1
    FactorTwo = np.matmul(UminusConTrans , Uplus) #U* times U+
    A = np.matmul( FactorOne , FactorTwo) #(u^* times U- )^-1 (U* times U+)
    eigenV = np.linalg.eig(A)[0] #computes an eigen Decomposition and returns eigenvalues
    Xi_Answer = np.array([cmath.log(ev)*(len(X)) for ev in eigenV],complex) #ln on each eigenvalue and scale values back to size
    return np.sort(Xi_Answer)