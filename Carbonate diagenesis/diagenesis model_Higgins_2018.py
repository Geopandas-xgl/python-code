#
import matplotlib.pyplot as plt
import numpy as np
F = 0.5 #孔隙度
densitys = 1.8 #碳酸盐岩密度 g/cm3 
densityf = 1.0125 #流体的密度 g/cm3
U = 10 #流速 cm/yr
percentU = 0.1 #假设box为1m，则每年流体流动的距离占比为0.1
Ro = 0.1 #反应速率 myr-1
deltaso = -1.6 #碳酸盐岩（？）中初始的Ca同位素值
deltafo = 0    #流体的初始同位素值
Cfo = 424   # 初始流体中的Ca的浓度(ppm)
delta = 0  #固相和液相之间的分馏值
Cso = [390000, 200000] # 固相中的初始Ca浓度
config = {"font.family":"serif",
          "font.serif": ["Times New Roman"],
          "font.size":"10"}
plt.rcParams.update(config)
Yarray = np.zeros((100,100000))
Xarray = np.zeros((100,100000))

for i in Cso:
    N = 0
    j = i
    k = Cso.index(i)
    X = []
    Y = []
    deltaf = deltafo
    to = 1000 #流体从1BOX至NBOX所需要的时间
    R = Ro/1000 # 1千年对应的反映速率
    t = to
    while N < 100: 
        mass_s = 1
        ratio_sum = 0
        Ydeltab = []
        Xdeltab = []
        M = 1
        X.append(N)
        Y.append(deltaf)
        deltaf = (percentU*t*(Cfo*densityf*F)*deltaf + R*(i*densitys*(1-F))*(deltaso-delta))/(percentU*t*(Cfo*densityf*F)+R*(i*densitys*(1-F)))
        deltafo_N = deltaf
        M_sed = i*densitys*(1-F)
        while M < 100001:
            ratio_a = mass_s*R
            ratio_sum =  ratio_sum + ratio_a 
            mass_s = 1 - ratio_sum
            M_sed = (1-R)*M_sed
            deltaf_N = (percentU*t*(Cfo*densityf*F)*deltafo_N + M_sed*(deltaso-delta))/(percentU*t*(Cfo*densityf*F)+ M_sed)
            deltasb = (deltaf_N+delta)*ratio_sum + deltaso*mass_s
            Ydeltab.append(deltasb)
            Xdeltab.append(M)
            M = M + 1
        Yarray[N,:] = np.array(Ydeltab)
        Xarray[N,:] = np.array(Xdeltab)
        N = N + 1   
        
    if 0 == k:
        plt.subplot(2,2,1)
        plt.title("Ca concentration_390000 ppm")
        plt.plot(X,Y)
        plt.subplot(2,2,2)
        plt.title("Ca concentration_390000 ppm")
        plt.xscale('log')
        plt.plot(Xarray[0,:],Yarray[0,:])
        plt.plot(Xarray[99,:],Yarray[99,:])
        
    else:
        plt.subplot(2,2,3)
        plt.title("Ca concentration_200000 ppm")
        plt.plot(X,Y)
        plt.subplot(2,2,4)
        plt.title("Ca concentration_200000 ppm")
        plt.xscale('log')
        plt.plot(Xarray[0,:],Yarray[0,:])
        plt.plot(Xarray[99,:],Yarray[99,:])
plt.tight_layout()
plt.savefig("C:\\Users\\19328\\Desktop\\西交测样\\成岩模拟\\Diagenesis model_Higgins_2018.jpg", dpi =600, format="jpg")
plt.show()



        



        
 