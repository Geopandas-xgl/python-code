# U同位素与U（IV）占比二元图
import matplotlib.pyplot as plt
import numpy as np
import xlrd
data = xlrd.open_workbook("C:\\Users\\19328\\Desktop\\西交测样\\成岩模拟\\NK-1数据.xlsx")
sheet = data.sheet_by_name("Sheet1")
R = sheet.col_values(2)
deltau = sheet.col_values(3)
a = np.array([0.4,0.6,0.8,1])
F = np.array([0.3,0.6,0.9,1.2]) #白云岩中初始的U含量的平均值
R_range = np.arange(0.1,1,0.02)
deltap = -0.25 #XK中纯白云岩U含量小于0.872的U同位素值的平均值

config = {"font.family":"serif",
          "font.serif": ["Times New Roman"],
          "font.size":"10"}
plt.rcParams.update(config)
for j in a:
    deltab = R_range*j + deltap
    plt.plot(R_range,deltab)
plt.plot(R[1:],deltau[1:],"bo",markersize=4)
plt.xlabel("U(IV)/(U(IV)+U(VI))")
plt.ylabel("δ$^{238}$U (‰)")
plt.xlim(0.1,1)
plt.ylim(-0.4, 0.6)
plt.xticks(np.arange(0.1,1,0.1))
plt.yticks(np.arange(-0.4,0.6,0.2))
plt.legend([0.4,0.6,0.8,1],loc = "lower right" ) 
plt.savefig("C:\\Users\\19328\\Desktop\\西交测样\\成岩模拟\\isotope_dolomite_NK-2.jpg", dpi =600, format="jpg")
plt.show()


