#每次迭代液相与部分固相（1-1/20）之间达到平衡，且平衡之后固相内部的同位素及含量分布均匀
import matplotlib.pyplot as plt
import numpy as np
F = 0.5 #液相占全岩的质量比
Rso = 0.708 #方解石初始Sr同位素比值 
Cse = 200 # 达到平衡时方解石中的Sr浓度
Cfo = 10  # 初始流体中的Sr的浓度
Rse = 0.72 # 达到平衡时方解石中的Sr同位素比值
IEQ = 0 #某水岩比值时对应的固相Sr同位素比值与初始固相Sr比值之差比上达到平衡时固相Sr比值与初始固相Sr比值之差
a = 1 #
D = 20 #方解石与液相之间分配系数
Cso = [40,1000] # 固相中的初始Sr浓度
config = {"font.family":"serif",
          "font.serif": ["Times New Roman"],
          "font.size":"10"}
plt.rcParams.update(config)
for i in Cso:
    EQ = 0
    m = Cso.index(i)
    Cf = Cfo
    box_Rf = []
    box_Cf = []
    Rfo = 0.72 # 液相中的初始Sr同位素比值
    RY_array = np.zeros((20,1000))
    Y_array = np.zeros((20,1000))
    X_array = np.zeros((20,1000))
    for j in range(1,21):
        k = 1/j
        t = j-1
        Z = []
        Y = []
        X = []
        N = 1
        h = Rso
        d = i
        while N <= 1000:
            Co = F*Cfo + (1-F)*k*d
            Ro = (Cfo*Rfo*F + h*d*(1-F)*k)/Co
            Cs = Co/(F/D+(1-F)*k)
            Rs = Ro*Co/(Cs*(F/(a*D)+(1-F)*k))
            Cb = (1-k)*d + k*Cs
            Rb = ((1-k)*d*h + k*Cs*Rs)/Cb
            d = Cb
            h = Rb
            N = N + 1
            Z.append(Rb)
            X.append(N)
            Y.append(Cb)
        RY_array[t,:] = Z
        Y_array[t,:] = Y
        X_array[t,:] = X
    if 0 == m:
        plt.subplot(2,2,1)
        plt.xscale('log')
        plt.title("Sr concentration_40 ppm")
        plt.plot(X_array[0,:],Y_array[0,:])
        plt.plot(X_array[9,:],Y_array[9,:])
        plt.plot(X_array[19,:],Y_array[19,:])
        plt.subplot(2,2,3 )
        plt.xscale('log')
        plt.plot(X_array[0,:],RY_array[0,:])
        plt.plot(X_array[9,:],RY_array[9,:])
        plt.plot(X_array[19,:],RY_array[19,:])
        plt.title("Sr ratio_40 ppm")
    else:
        plt.subplot(2,2,2)
        plt.xscale('log')
        plt.title("Sr concentration_1000 ppm")
        plt.plot(X_array[0,:],Y_array[0,:])
        plt.plot(X_array[9,:],Y_array[9,:])
        plt.plot(X_array[19,:],Y_array[19,:])
        plt.subplot(2,2,4)
        plt.xscale('log')
        plt.title("Sr ratio_1000 ppm")
        plt.plot(X_array[0,:],RY_array[0,:])
        plt.plot(X_array[9,:],RY_array[9,:])
        plt.plot(X_array[19,:],RY_array[19,:])
plt.tight_layout()
plt.savefig("C:\\Users\\19328\\Desktop\\西交测样\\成岩模拟\\Diagenesis model_banner_1990_1.jpg", dpi =600, format="jpg")
plt.show()


        



        
 