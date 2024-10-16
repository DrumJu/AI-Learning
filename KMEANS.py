import numpy as np
import matplotlib.pyplot as plt
import random
data=np.loadtxt('SIZE DATA.txt',delimiter=',')
num=int(data.size/2)
def distance(a,b):
    return np.sum((a-b)**2,axis=1)**0.5
def Kmeans(k,X):
    idx=random.sample(list(range(num)),k)
    clusters=X[idx]
    labels=np.zeros(num)
    while True:
        count=0
        i=0
        for d in X:
            dst=distance(d,clusters)
            min_idx=np.argmin(dst)
            if labels[i]!=min_idx:
                count+=1
                labels[i]=min_idx
            i+=1
        if count==0:
            break
        for label in range (k):
            centroid=np.mean(X[labels==label],axis=0)
            clusters[label]=centroid
    return labels
print(Kmeans(4,data))
#labels=Kmeans(4,data)
#plt.scatter(data[:,0],data[:,1],c=labels)
#plt.show()
#可视化
