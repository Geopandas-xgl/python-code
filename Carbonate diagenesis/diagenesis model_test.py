import matplotlib.pyplot as plt
import numpy as np

dv = np.arange(0.4, 0.71, 0.1)
F = np.arange(0,1.1,0.1)
deltar = -0.39
config = {"font.family":"serif",
          "font.serif": ["Times New Roman"],
          "font.size":"10"}
for i in dv:
    deltam = deltar + F*i
    plt.plot(F, deltam)
plt.xlabel("F") #(溶解占比)
plt.ylabel("δ$^{238}$U (‰)")
plt.legend([0.4,0.5,0.6,0.7],loc = "upper left" ) 
plt.savefig("C:\\Users\\19328\\Desktop\\西交测样\\成岩模拟\\diagenesis model_test.jpg", dpi =600, format="jpg")
plt.show()

