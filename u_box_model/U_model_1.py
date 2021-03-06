import matplotlib.pyplot as plt

# U mass sst up
duration = 2e6
dt = 500
t = list(range(0, int(duration), dt))

sw_conc = list(range(len(t)+1))
sw_moles = list(range(len(t)+1))
carb_conc = list(range(len(t)+1))
sw_conc[0]=3.3
ocean_mass = 1.41357575757576e21
M_riv = 0.4e8
extent = 0.0021
K_a = 1.45772594752187e-4 #calculated
K_o = 1.73834440079269e-6 #calculated to reach steady state
D_u = 1.4 #partition coefficient factor to convert from moles cc to moles sw #1.6 original
sw_moles[0]=(sw_conc[0]*ocean_mass/(1e6*238)) #coverts ppb to moles U


# U isotope set up
d238U = list(range(len(t)+1))
d238U[0] = -0.165
dUriv = 0.05
Frac_a = 0.6
Frac_o = 0.0294118

# time set up
carb1 = []
carb2 = []
carb3 = []
carb4 = []
d1 = []
d2 = []
d3 = []
d4 = []
dUriv1 = []
dUriv2 = []
dUriv3 = []
dUriv4 = []
Uriv1 = []
Uriv2 = []
Uriv3 = []
Uriv4 = []
fanox1 = []
fanox2 = []
fanox3 = []
fanox4 = []

# model equations
for j in range(0, 4):
    for  i in range(0, len(t)):
        if i <= 718:
            extent = 0.0021
            M_riv = 0.4e8
            dUriv = -0.05
        elif  i>718 & i<=780:
            if j == 0:
                extent = 0.2
            elif j == 1:
                M_riv = 0.4e7
                dUriv = -0.8
            elif j == 2:
                dUriv = -0.8
            elif j == 3:
                M_riv = 0.4e9
                dUriv = -0.8
        else:
            if j == 0:
                extent = 0.5
        M_anox = sw_moles[i]*K_a*extent
        M_other = sw_moles[i]*K_o*(1-extent)
        sw_moles[i+1] = sw_moles[i] + (M_riv - M_anox - M_other)*dt
        sw_conc[i+1] = sw_moles[i+1]*1e6*238/ocean_mass
        carb_conc[i+1] = sw_conc[i+1]/D_u
        Iso_riv = M_riv*(dUriv-d238U[i])/sw_moles[i]
        Iso_anox = M_anox*Frac_a/sw_moles[i]
        Iso_other = M_other*Frac_o/sw_moles[i]
        d238U[i+1] = (d238U[i]+(Iso_riv-Iso_anox-Iso_other)*dt)

        if j == 0:
            carb1.append(carb_conc[i+1])
            d1.append(d238U[i+1])
            dUriv1.append(dUriv)
            Uriv1.append(M_riv)
            fanox1.append(extent)
        elif j ==1:
            carb2.append(carb_conc[i+1])
            d2.append(d238U[i+1])
            dUriv2.append(dUriv)
            Uriv2.append(M_riv)
            fanox2.append(extent)
        elif j ==2:
            carb3.append(carb_conc[i+1])
            d3.append(d238U[i+1])
            dUriv3.append(dUriv)
            Uriv3.append(M_riv)
            fanox3.append(extent)
        elif j ==3:
            carb4.append(carb_conc[i+1])
            d4.append(d238U[i+1])
            dUriv4.append(dUriv)
            Uriv4.append(M_riv)
            fanox4.append(extent)
#plots
# stacked figure
plt.axes(xscale = 'log')
plt.xlabel('[U](ppm)')
plt.ylabel('Time(yr)')
plt.xlim(0.05, 30)
plt.plot(carb1, t, c='red', linestyle='-')
plt.plot(carb2, t, c='blue', linestyle='--')
plt.plot(carb3, t, c='green', linestyle=':')
plt.plot(carb4, t, c='orange', linestyle='-')
plt.show()

plt.xlabel('d238U')
plt.ylabel('Time (yr)')
plt.plot(d1, t, c='red', linestyle='-')
plt.plot(d2, t, c='blue', linestyle='--')
plt.plot(d3, t, c='green', linestyle=':')
plt.plot(d4, t, c='orange', linestyle='-')
plt.show()
