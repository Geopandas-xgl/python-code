import matplotlib.pyplot as plt
import  numpy as np

K_Mg = 10**4.27
K_Ca1 = 10**5.34
K_Ca2 = 10**3.8
C_Ca = np.arange(0,200) #Ca离子浓度从0至60 mMol
C_Mg = 50 #Mg离子浓度为50 mM;

alph =0.32*(1/(1 + K_Ca1/(C_Ca*K_Ca2) + K_Mg*C_Mg/((C_Ca**2)*K_Ca2)))

plt.plot(C_Ca, alph)
 

