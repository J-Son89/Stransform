import matplotlib.pyplot as plt
import pandas as pd
import sys


def mergeFile(scale):
	frames =[]
	for i in range(1,5,1):
		frames.append(pd.read_csv('scale' +str(scale) + 'test_'+ str(i) +'.csv', sep=',',header=None, index_col =0))
	return pd.concat(frames)

result = mergeFile(sys.argv[1])

##direction of weigghted norm
y,n=0,0
for i in result[4]:
	if(i<0):
		n+=1
	else:
		y+=1

rankC,rankW=0,0
for i in result[5]:
	if(i==8):
		rankC+=1
	else:
		rankW+=1

print('better:',y,'worse:',n)
print('correctRank:',rankC,'wrongRank',rankW)
#print(result[4])
#plt.ylabel('Frequency')
#plt.xlabel('Words')
#plt.title('Title')

#plt.show()