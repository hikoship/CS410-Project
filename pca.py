# Data: 22215(dimension) * 192(sample)
from time import *
from matplotlib.mlab import PCA
#import numpy as np
from numpy import *
import matplotlib.pyplot as plt 

def pca(dataMat, topNfeat=9999999):  
    meanVals = mean(dataMat)  
    meanRemoved = dataMat - meanVals #remove mean  
    covMat = cov(meanRemoved, rowvar=0)  
    eigVals,eigVects = linalg.eig(mat(covMat))  
    eigValInd = argsort(eigVals)            #sort, sort goes smallest to largest  
    eigValInd = eigValInd[:-(topNfeat+1):-1]  #cut off unwanted dimensions  
    redEigVects = eigVects[:,eigValInd]       #reorganize eig vects largest to smallest  
    lowDDataMat = meanRemoved * redEigVects#transform data into new dimensions  
    #reconMat = (lowDDataMat * redEigVects.T) + meanVals  
    return lowDDataMat  

def plotBestFit(dataSet1,dataSet2):        
    dataArr1 = array(dataSet1)  
    dataArr2 = array(dataSet2)  
    n = shape(dataArr1)[0]   
    n1=shape(dataArr2)[0]  
    xcord1 = []; ycord1 = []  
    xcord2 = []; ycord2 = []  
    xcord3=[];ycord3=[]  
    j=0  
    for i in range(n):  
          
            xcord1.append(dataArr1[i,0]); ycord1.append(dataArr1[i,1])  
            xcord2.append(dataArr2[i,0]); ycord2.append(dataArr2[i,1])                    
    fig = plt.figure()  
    ax = fig.add_subplot(111)  
    ax.scatter(xcord1, ycord1, s=30, c='red', marker='s')  
    ax.scatter(xcord2, ycord2, s=30, c='green')  
      
    plt.xlabel('X1'); plt.ylabel('X2');  
    plt.show() 

datafile = open('postdata2.txt')
data = [[0 for j in range(2221)] for i in range(192)]
i = 0
for line in datafile:
    j = 0
    sampleList = line.split()
    for sample in sampleList:
        # i: dimension -> column
        # j: sample -> row
        data[j][i] = float(sample)
        j += 1

    i += 1

dataMatrix = matrix(data)
#dataMatrix = dataMatrix.transpose()
b= pca(dataMatrix, 200)
print b
b = b.tolist()

#print time()
#print(localtime(time()))
print len(data)
print clock()

fout = open('output3.txt', 'w')
for line in b:
    for e in line:
        fout.write('%s\t' % e)
    fout.write('\n')
fout.close()
