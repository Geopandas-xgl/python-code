import matplotlib.pyplot as plt
import math 
F = 0.5 #液相占全岩的质量比
N = F/(1-F) #液相和固相的质量比
Cfo = 500
D =  4138
deltafo = 2
deltaso = 4.8
Cso = [120002,12000]
dv = 1

config = {"font.family":"serif",
          "font.serif": ["Times New Roman"],
          "font.size":"10"}

plt.rcParams.update(config)
for Cs in Cso:
    deltas = deltaso
    i = 1
    j = Cs
    k = Cso.index(Cs)
    X = []
    YCs = []
    Ydeltas = []
    #EQ = 0
    
    while i <= 100000:
        deltas = (((Cs/Cfo)*deltas + D*(math.exp(N/D)-1)*(dv + deltafo))/
        ((Cs/Cfo)+D*(math.exp(N/D)-1)))
        Cs = D*Cfo + (Cs-D*Cfo)*math.exp(-N/D)
        Ydeltas.append(deltas)
        YCs.append(Cs)
        X.append(i)
        i = i + 1
    if 0 == k:
        plt.subplot(2,2,1)
        plt.xscale('log')
        plt.title("C concentration_120000 ppm")
        plt.plot(X,YCs)
        plt.subplot(2,2,2 )
        plt.xscale('log')
        plt.plot(X,Ydeltas)
        plt.title("C isotope_120000 ppm")
    else:
        plt.subplot(2,2,3)
        plt.xscale('log')
        plt.title("C concentration_12000 ppm")
        plt.plot(X,YCs)
        plt.subplot(2,2,4)
        plt.xscale('log')
        plt.title("C isotope_12000 ppm")
        plt.plot(X,Ydeltas)
plt.tight_layout()
plt.savefig("C:\\Users\\19328\\Desktop\\西交测样\\成岩模拟\\Diagenesis model_chen_2018_2.jpg", dpi =600, format="jpg")
plt.show()


        



        
 