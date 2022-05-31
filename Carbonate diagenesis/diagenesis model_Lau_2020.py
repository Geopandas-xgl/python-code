import matplotlib.pyplot as plt
import math
import numpy as np

Kmax = math.pow(10,-10.3) # mol/kg/yr
Ks = 4.99e-4 #mol/kg
Kin = 1e-6 #mol/kg
O = 1e-6 #mol/Kg
U = np.array([20,14,10,1])/1e9 #mol/kg

R = -Kmax*(U/(U+Ks))*(Kin/(Kin+O)) #mol/kg/yr

r_1 = R*1e9*1.8e3/3.15576e7 #nmol/m3/s

r = R*1*238*1000*502/(900*1e-5) #ppm







 

