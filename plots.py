import matplotlib.pyplot as plt
import numpy as np
import cmath
def PolarPlot(M,i):
    plt.figure(i)
    for i in range(M.shape[1]):
        for j in range(M.shape[0]):
            plt.polar([0,np.angle(M[i,j])],[0,abs(M[i,j])],marker='o')    
    plt.show

#plot singular values
def SVPlot( array, style, i ,title):
    plt.figure(i)
    x = np.linspace(0,len(array),len(array))
    plt.plot(x,array, style)
    plt.show
    plt.title(title)
    
def PlotFrequencies(array,a,b,style,i,name):
    plt.figure(i)
    plt.figure(i).set_size_inches(14.5, 8.5, forward=True)
    x = np.linspace(a,b,len(array))
    plt.plot(x,array.real,style)  
    plt.show
    plt.title(name)
    #build plot for frequencies


def h(xj,x):
    return np.array([ (cmath.exp((xj[j]) * (x))) for j in range(len(xj)) ],complex)
    
def xi(XI,a,b, Len):
    x = np.linspace(a,b, Len )
    plt.figure(56)
    plt.figure(56).set_size_inches(9, 8, forward=True)
    A= np.array([h(XI,xi) for xi in x ],complex ) 
    plt.imshow(A.real, cmap='viridis',extent=[-(Len-1)/2,(Len-1)/2,a,b], aspect='auto')
    plt.figsize=(9.3, 6)
    plt.tight_layout()
    plt.show()
    plt.figure(57)
    plt.figure(57).set_size_inches(9, 8, forward=True)
    A= np.array([h(XI,xi) for xi in x ],complex ) 
    plt.imshow(A.imag, cmap='viridis',extent=[-(Len-1)/2,(Len-1)/2,a,b], aspect='auto')
    plt.figsize=(9.3, 6)
    plt.tight_layout()
    plt.show()