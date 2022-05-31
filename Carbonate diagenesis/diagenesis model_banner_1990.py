import matplotlib.pyplot as plt
F = 0.5 #液相占全岩的质量比
Rso = 0.708 #方解石初始Sr同位素比值 
Cse = 200 # 达到平衡时方解石中的Sr浓度
Cfo = 10  # 初始流体中的Sr的浓度
Rf = 0.72 # 液相中的初始Sr同位素比值
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
    j = i
    N = 0
    EQ = 0
    k = Cso.index(i)
    X = []
    Y = []
    RY = []
    Rs = Rso
     
    while N <= 1000:      
        Co = F*Cfo + (1-F)*i
        Ro = (Rf*Cfo*F + Rs*i*(1-F))/Co
        i = Co/(F/D+(1-F))
        Rs = Ro*Co/(i*(F/(a*D)+1-F))
        N = N + 1
        EQ = (i-j)/(Cse-j)
        IEQ = (Rs-Rso)/(Rse-Rso)
        RY.append(Rs)
        X.append(N)
        Y.append(i)
    if 0 == k:
        plt.subplot(2,2,1)
        plt.xscale('log')
        plt.title("Sr concentration_40 ppm")
        plt.plot(X,Y)
        plt.subplot(2,2,3 )
        plt.xscale('log')
        plt.plot(X,RY)
        plt.title("Sr ratio_40 ppm")
    else:
        plt.subplot(2,2,2)
        plt.xscale('log')
        plt.title("Sr concentration_1000 ppm")
        plt.plot(X,Y)
        plt.subplot(2,2,4)
        plt.xscale('log')
        plt.title("Sr ratio_1000 ppm")
        plt.plot(X,RY)
plt.tight_layout()
plt.savefig("C:\\Users\\19328\\Desktop\\西交测样\\成岩模拟\\Diagenesis model_banner_1990.jpg", dpi =600, format="jpg")
plt.show()


        



        
 