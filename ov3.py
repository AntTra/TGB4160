import matplotlib.pyplot as plt
import numpy as np

# Geological time steps (Ma)
x = np.array([0, 25, 55, 65, 100, 140, 160])

# Burial depth histories
upper_jurassic = np.array([1000+750+250+750+500+250, 750+250+750+500+250, 250+750+500+250, 
                           750+500+250, 500+250, 250, 0])
lower_cretaceous = upper_jurassic - np.full(7, 250) 
upper_cretaceous = lower_cretaceous - np.full(7, 500) 
palaeocene = upper_cretaceous - np.full(7, 500)
oligocene = palaeocene - np.full(7, 500) 
miocene = oligocene - np.full(7, 750, dtype=int) 

# Setup plot
figu, axe = plt.subplots(figsize=(9,6))
axe.invert_yaxis()
axe.set_ylim(3600, 0) 
axe.invert_xaxis()

# Burial history curves
axe.plot(x, miocene, label = 'miocene') 
axe.plot(x, oligocene, label = 'oligocene') 
axe.plot(x, palaeocene, label = 'Palaeocene') 
axe.plot(x, upper_cretaceous, label = 'Upper cretaceous')
axe.plot(x, lower_cretaceous, label = 'Lower cretaceous') 
axe.plot(x, upper_jurassic, label = 'Upper jurassic')

# Temperature isotherms (depths)
temps = [60, 100, 160]
depths = [(T - 20)/0.04 for T in temps]  # convert °C to depth (m)

# Shade oil window (1000–3500 m)
axe.axhspan(depths[0], depths[2], facecolor='khaki', alpha=0.3, label="Oil window")

# Shade gas window (>3500 m) - here we just mark below 3500
axe.axhspan(depths[2], 3600, facecolor='lightcoral', alpha=0.3, label="Gas window")

# Draw isotherm lines
for T, z in zip(temps, depths):
    axe.hlines(y=z, xmin=0, xmax=160, colors='k', linestyles='--', label=f'{T} °C')

# Labels and legend
axe.set_xlabel("Geologic Time (Ma)")
axe.set_ylabel("Burial Depth (m)")
axe.set_title("Exercise 3A: Burial History Graph with Isotherms")
axe.grid(True)
axe.legend(loc="best")

plt.show()