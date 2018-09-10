##files
import config
import esprit
import s_transform
import leastSquares
import functions
#import plots
##packages
import numpy as np
import pandas as pd
import sys
#import prof
#profile = prof.profile 
testNo =sys.argv[1] if len(sys.argv) >1 else 1 
file_out = sys.argv[2]
results = { "test_No": testNo,"Scale of Noise":config.scale, "rho":config.rho}
##set up
mu = config.mu # Paramter to increase/decrease impact of High Rank Penalty
rho = config.rho # Tweaks Convergnce of ADMM
N = config.N
a,b= config.a,config.b

##Frequencies
SV = config.SV #F(x) without noise
SVN= SV + config.Fuzz #F(x)
Hf= config.Hf # noise free Hankel; F(x)-n(x)
HfN=config.HfN; #Hankel with noise; F(x)

c=0
X,Y,Lambda =1,0,0


def main(X,Y,Lambda,c):
    while(np.linalg.norm(X-Y)>10**-12 and c<13000):
        X,Y,Lambda = s_transform.ADMM(X,Y,Lambda,HfN)
        c+=1
    
#    print('number of iterations',c)
    
    return X,Y,Lambda,c

X,Y,Lambda,c= main(X,Y,Lambda,c)
if(c >12000):
    c = "NA"
results["rank_of_X"] = int(np.linalg.matrix_rank(X) )
results["#_of_iterations"] = c
#runs ESPRIT ON X; returns #Xihat
XiHat = esprit.Esprit(X) 
# make vector from X, flipped columns so antidiagonals are diagonals
HfNHat = functions.hankelToVect( X[:, ::-1], N) 
#Least squares with vector from X Hankel
CHat = leastSquares.getConstants(XiHat,HfNHat,a,b)

##Just ESPRIT on F(x)
Xi_Esprit = esprit.Esprit(HfN)
##Least squares approx on F(x)
C_Esprit = leastSquares.getConstants(Xi_Esprit,SVN,a,b)

ST = functions.ApproxVector(2*N+1,-1,1,XiHat,CHat)  #noise X
ESP = functions.ApproxVector(2*N+1,-1,1,Xi_Esprit,C_Esprit) #NOISE NO FILTER

HfHat = functions.vectToHankel(ST,N) #Hankel from sum of exponentials w/ XiHat and Chat
ESPmatrix = functions.vectToHankel(ESP,N) #Hankel with ... .. XiEsprit + CEsprite

results["norm_dif"] = float((np.linalg.norm(ST-SVN) - np.linalg.norm(ESP - SVN) ) /np.linalg.norm(SVN))
results["weighted_norm_dif"]=float((np.linalg.norm(HfHat-HfN) - np.linalg.norm(ESPmatrix - HfN) )/np.linalg.norm(HfN))

results["outcome"] =  1 if results["weighted_norm_dif"] <0 else -1

MyLilPanda = pd.DataFrame.from_records(results, index=[0])
with open(file_out, 'a') as f:
    MyLilPanda.to_csv(f, header=False)


###Plots
#title = '(yellow) - No noise VS noise - (red)'
#plots.PlotFrequencies(SV,a,b,'y-', c+2,title)
#plots.PlotFrequencies(SVN,a,b,'r-', c+2,title) 
#
#
#title = '#(yellow) S-transform VS Ground Truth (Green) Vs ESPRIT (Red) '
## Y with noise vs Samples
#
#plots.PlotFrequencies(ST,a,b,'y-', c+6,title)
#plots.PlotFrequencies(SV,a,b,'g-', c+6,title)
#plots.PlotFrequencies(ESP,a,b,'r-', c+6,title)
##plots.PlotFrequencies(AV3N,a,b,'b-', c+6,title)
#
#plots.SVPlot(np.sort(Xi_Esprit),'ro', c+3,title)
#plots.SVPlot(np.sort(XiHat),'yo', c+3,title) #red = s trans (XN)
#plots.SVPlot(np.sort(config.Xi),'go',c+3,title) #green = actual
#
#
#title = '#(yellow) S-transform VS Vs GT +Noise (green)' 
#plots.PlotFrequencies(ST,a,b,'y-', c+7,title)
#plots.PlotFrequencies(SVN,a,b,'g-', c+7,title)
#
#