import matplotlib.pyplot as plt
import numpy as np
import xlrd
data = xlrd.open_workbook("C:\\Users\\19328\\Desktop\\西交测样\\成岩模拟\\NK-1数据.xlsx")
sheet = data.sheet_by_name("白云岩段_f reduce_isotope")
cu = sheet.col_values(3)
deltau = sheet.col_values(4)
a = np.arange(0.1,0.61,0.1)
F = np.arange(0.5,1.01,0.166)
cb = np.arange(0.872,20,0.02)
deltap = -0.25 #XK中纯白云岩U含量小于0.872的U同位素值的平均值
cp = 0.872 #XK中白云岩U含量的平均值
config = {"font.family":"serif",
          "font.serif": ["Times New Roman"],
          "font.size":"10"}
plt.rcParams.update(config)
for i in F:
    n = list(np.where(F == i))
    for j in a:
        deltab = (1-cp/cb*i)*j + deltap
        plt.subplot(2,2,n[0] + 1)
        plt.plot(cb,deltab)
    plt.xscale('log')
    plt.xlabel("U (ppm)")
    plt.ylabel("δ238U (‰)")
    plt.xlim(1,20)
    plt.ylim(-0.6, 0.6)
    plt.xticks([1,10])
    plt.yticks(np.arange(-0.6,0.6,0.2))
    plt.tight_layout()
    plt.subplot(2,2,n[0] + 1)
    plt.plot(cu[1:],deltau[1:],"bo",markersize=4 )
plt.legend([0.1,0.2,0.3,0.4,0.5,0.6],loc = "upper left" ) 
plt.savefig("C:\\Users\\19328\\Desktop\\西交测样\\成岩模拟\\isotope_dolomite_NK-1.jpg", dpi =600, format="jpg")
plt.show()


