import matplotlib.pyplot as plt
import numpy as np
from numpy.ma import exp 
N = np.logspace(-3,5,num = 1000)
Cfo = np.array([29,1000,889000,889000,400,100,0.001,0.0015,8,4,0.003,0.003,0.0005,0.0005])
D =  np.array([4138,4138,0.54,0.54,1000,1000,20000,12000,300,360,200,160,200000,200000])
deltafo = np.array([2,-10,-29.3,-34.2,np.NaN,np.NaN,np.NaN,np.NaN,np.NaN,np.NaN,-0.39,-0.34,-0.39,-0.34])  
deltaso = np.array([4.8,4.8,0.5,0.5,np.NaN,np.NaN,np.NaN,np.NaN,np.NaN,np.NaN,-0.37,-0.37,-0.37,-0.37])
Cso = np.array([120000,120000,480000,480000,400000,400000,3,3,4500,4500,3,3,3,3]) 
dv = np.array([1,1,32,32,np.NaN,np.NaN,np.NaN,np.NaN,np.NaN,np.NaN,0.1,0.03,1,1])


config = {"font.family":"serif",
          "font.serif": ["Times New Roman"],
          "font.size":"10"}
plt.rcParams.update(config)



X = []
YCs = np.zeros((1000,14))
Ydeltas = np.zeros((1000,14))
for  i in N:
    j =np.where(N == i)
    deltas = (((Cso/Cfo)*deltaso + D*(exp(i/D)-1)*(dv + deltafo))/
    ((Cso/Cfo)+D*(exp(i/D)-1)))
    Cs = D*Cfo + (Cso-D*Cfo)*exp(-i/D)
    Ydeltas[j,:] = deltas
    YCs[j,:] = Cs
    X.append(i)


plt.subplot(2,3,1)
plt.xscale('log')
plt.title("C Isotope")
plt.xlim(0.01,100000)
plt.plot(X,Ydeltas[:,0])
plt.plot(X,Ydeltas[:,1])


plt.subplot(2,3,2)
plt.xscale('log')
plt.title("O isotope")
plt.xlim(0.001,100000)
plt.plot(X,Ydeltas[:,2])
plt.plot(X,Ydeltas[:,3])

plt.subplot(2,3,3)
plt.xscale('log')
plt.title("Mn concentration")
plt.xlim(0.001,100000)
plt.plot(X,YCs[:,6])
plt.plot(X,YCs[:,7])

plt.subplot(2,3,4)
plt.xscale('log')
plt.title("Sr concentration")
plt.xlim(0.001,100000)
plt.plot(X,YCs[:,8])
plt.plot(X,YCs[:,9])

plt.subplot(2,3,5)
plt.xscale('log')
plt.title("U isotope")
plt.xlim(0.001,100000)
plt.plot(X,Ydeltas[:,10])
plt.plot(X,Ydeltas[:,11])
plt.ylim(-0.4,-0.2)
#plt.plot(X,Ydeltas[:,12])
#plt.plot(X,Ydeltas[:,13])

plt.subplot(2,3,6)
plt.xscale('log')
plt.title("U concentration")
plt.xlim(0.001,100000)
plt.plot(X,YCs[:,10])
plt.plot(X,YCs[:,11])
plt.plot(X,YCs[:,12])
plt.plot(X,YCs[:,13])

plt.tight_layout()
plt.savefig("C:\\Users\\19328\\Desktop\\西交测样\\成岩模拟\\Diagenesis model_chen_2018_3.jpg", dpi =600, format="jpg")
plt.show()


plt.plot(Ydeltas[:,2],Ydeltas[:,0])
plt.plot(Ydeltas[:,3],Ydeltas[:,1])
plt.show()

        



        
 