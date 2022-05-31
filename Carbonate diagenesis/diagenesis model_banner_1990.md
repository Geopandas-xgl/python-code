#  Diagenesis model_banner_1990

水岩平衡反应过程，不同初始Sr浓度的固相解石中Sr元素及同位素对蚀变的敏感度

## Introduction

1. 模型采用的间断式完全平衡模式，
   
   *  每一次反应固相与液相能都达到完全平衡
   *  不同次反应之间流体的元素的含量和同位素组成不变
   *  使用迭代法
2. 模型中使用到的基本公式：
3. 模型来源：

![image](https://user-images.githubusercontent.com/83357799/162007114-f08c29ed-2b12-40a9-9b0d-0b5e2ba7e80a.png)


## Code

```python
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
        plt.title("Sr isotope_40 ppm")
    else:
        plt.subplot(2,2,2)
        plt.xscale('log')
        plt.title("Sr concentration_1000 ppm")
        plt.plot(X,Y)
        plt.subplot(2,2,4)
        plt.xscale('log')
        plt.title("Sr isotope_1000 ppm")
        plt.plot(X,RY)
plt.tight_layout()
plt.savefig("C:\\Users\\19328\\Desktop\\西交测样\\成岩模拟\\Diagenesis model_banner_1990.jpg", dpi =600, format="jpg")
plt.show()

```

## Results

![Diagenesis model_banner_1990](https://user-images.githubusercontent.com/83357799/162006985-a85ef3ba-9320-418a-b080-876d90ad6738.jpg)


## Analyse

1. 低Sr方解石（40 ppm）和高Sr方解石（1000 ppm）发生同位素发生变化对应的低累计水岩比值分别为（1-10<sup>2 </sup> ）和（10-100），表明低Sr方解石更早地发生成岩蚀变。若仅仅考虑U含量，原始成因方解石（低U含量）确实较原始成因文石（高U含量）发生蚀变；
2. 优点：1. 模拟过程简单易懂，易操作；2. 定量描述随着水岩比值（蚀变）的增加，元素含量和同位素的变化。3. 可以定量同位素体系的封闭性对固相、液相元素含量及同位素比值的敏感度；
3. 缺点：1.实际的水岩反应过程中水岩之间难以完全达到平衡；2. 该模型中没有考虑反应速率的影响和流体流速的影响；3.实际反应过程是连续的，而不是间断的



