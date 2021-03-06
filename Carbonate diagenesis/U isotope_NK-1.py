import matplotlib.pyplot as plt
import numpy as np
import xlrd
data = xlrd.open_workbook("C:\\Users\\19328\\Desktop\\西交测样\\成岩模拟\\NK-1数据.xlsx")
#sheet = data.sheet_by_name("白云岩段_f reduce_isotope")
sheet = data.sheet_by_name("Sheet1")
#cu = sheet.col_values(3)
cu = sheet.col_values(1)
#deltau = sheet.col_values(4)
deltau = sheet.col_values(3)
a = np.arange(0.1,0.61,0.1)
F = np.arange(0,0.61,0.2)
cb = np.arange(0.872,20,0.02)
deltap = -0.25 #XK中纯白云岩U含量小于0.872的U同位素值的平均值
cp = 0.872 #XK中白云岩U含量的平均值
config = {"font.family":"serif",
          "font.serif": ["Times New Roman"],
          "font.size":"10"}
plt.rcParams.update(config)
for i in F:
    n = list(np.where(F == i))
    plt.subplot(2,2,n[0] + 1)
    for j in a:
        deltab = (1-cp/cb*(1-i))*j + deltap
        plt.plot(cb,deltab)
    plt.plot(cu[1:],deltau[1:],"bo",markersize=4 )
    plt.annotate("F = %.1f" %(i),xy = (2,0.4))
    plt.xlabel("U (ppm)")
    plt.ylabel("δ$^{238}$U (‰)")
    plt.xlim(1,15)
    plt.ylim(-0.6, 0.6)
    plt.xticks(range(1,15,2))
    plt.yticks(np.arange(-0.6,0.6,0.2))
    plt.tight_layout()
plt.legend([0.1,0.2,0.3,0.4,0.5,0.6],loc = "upper right" ) 
plt.savefig("C:\\Users\\19328\\Desktop\\西交测样\\成岩模拟\\isotope_dolomite_NK-1.jpg", dpi =600, format="jpg")
plt.show()


