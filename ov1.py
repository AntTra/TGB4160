import matplotlib.pyplot as plt
import numpy as np

# (deposition age, present depth)
units = {
    "Jurassic": (210, 5200),
    "Lower Cretaceous": (140, 4148),
    "Upper Cretaceous": (95, 3689),
    "Paleocene": (65, 2721),
    "Eocene & Younger": (55, 2116),
}
#  0, 605, 968, 459, 1052
#  0, 605, 1573, 2032, 3084
x = np.array([0, 55, 65, 95, 140, 160, 210])
eocene = np.array([5200, 5200-2116, 5200-2721, 5200-3689, 5200-4148, 5200-4148, 0])
palaeocene = np.array([4148, 4148-2116, 4148-2721, 4148-3689, 4148-4148, 4148-4148, 0])
upper_cretaceous = np.array([3689, 3689-2116, 3689-2721, 3689-3689, 4148-4148, 4148-4148, 0])
lower_cretaceous = np.array([2721, 2721-2116, 2721-2721, 0, 4148-4148, 4148-4148, 0])
jurassic = np.array([2116, 2116-2116, 2721-2721, 0, 4148-4148, 4148-4148, 0])

fig, ax = plt.subplots(figsize=(9,6))

#for name, (age, depth) in units.items():
#    ax.plot([age, 0], [0, depth], marker="o", label=name)
ax.plot(x, eocene, label = "Eocene")
ax.plot(x, palaeocene, label = "Palaeocene")
ax.plot(x, upper_cretaceous, label = "Upper cretaceous")
ax.plot(x, lower_cretaceous, label = "Lower cretaceous")
ax.plot(x, jurassic, label = "Jurassic")

#ax.plot(palaeocene)
ax.axvspan(140, 160, color="red", alpha=0.2, label="Unconformity (notice 20 myr missing)")

# Geology conventions
ax.invert_yaxis()
ax.set_ylim(5300, 0) 
ax.invert_xaxis()
ax.set_xlabel("Geologic Time (Ma)")
ax.set_ylabel("Burial Depth (m)")
ax.set_title("Exercise 1A: Burial History Graph")
ax.grid(True)
ax.legend(loc="best")

######################################
# ######################################################
x = np.array([0, 5, 23, 36, 57, 66, 97, 144, 169, 187, 208, 230, 245])
lower_triassic = np.array([3250, 2930, 2770, 2560, 2390, 1940, 1750, 1750 - 310, 1750, 1170, 990, 650, 0])

upper_triassic = lower_triassic - np.full(13, 320) - x
lower_jurassic = upper_triassic - np.full(13, 240) - x
middle_jurassic = lower_jurassic - np.full(13, 210) - x
upper_jurassic = middle_jurassic - np.full(13, 110) - x*1.5
lower_cretaceous = upper_jurassic - np.full(13, 130) + x*0.5
upper_cretaceous = middle_jurassic - np.full(13, 450) - x*1.5
palaeocene = upper_cretaceous - np.full(13, 190) - x*1.5
eocene = palaeocene - np.full(13, 580) - x
oligocene = eocene - np.full(13, 180) - x*1.5
miocene = oligocene - np.full(13, 340, dtype=int) - x
pliocene = miocene - np.full(13, 650, dtype=int) 

# # unit = {
# #     "Pliocene": (5, 650), 
# #     "Miocene": (23, 990),
# #     "Oliogocene": (36, 1170),
# #     "Eocene": (57, 1750),
# #     "Palaeocene": (66, 1940),
# #     "Upper Cretaceous": (97, 2390),
# #     "Middle Jurassic": (187, 2560),
# #     "Lower Jurassic": (208, 2770),
# #     "Upper Triassic": (230, 2930),
# #     "Lower Triassic": (245, 3250),
# # }

figu, axe = plt.subplots(figsize=(9,6))
axe.invert_yaxis()
axe.set_ylim(3300, 0) 
axe.invert_xaxis()
# for name, (age, depth) in unit.items():
#     axe.plot([age, depth], marker="o", label=name)
axe.plot(x, pliocene, label = 'pliocene')
axe.plot(x, miocene, label = 'miocene') 
axe.plot(x, oligocene, label = 'oligocene') 
axe.plot(x, eocene, label = 'eocene') 
axe.plot(x, palaeocene, label = 'Palaeocene') 
axe.plot(x, upper_cretaceous, label = 'Upper cretaceous')
axe.plot(x, lower_cretaceous, label = 'Lower cretaceous') 
axe.plot(x, upper_jurassic, label = 'Upper jurassic')
axe.plot(x, middle_jurassic, label = 'middle_jurassic')
axe.plot(x, lower_jurassic, label ='lower_jurassic')
axe.plot(x, upper_triassic, label = 'upper_triassic')
axe.plot(x, lower_triassic, label = 'lower_triassic')

axe.axvspan(187, 97, color="red", alpha=0.2, label="Uplift causing erosion of layers during this period")

# Geology conventions

#axe.set_xlim(245, 0) 

axe.set_xlabel("Geologic Time (Ma)")
axe.set_ylabel("Burial Depth (m)")
axe.set_title("Exercise 2A: Burial History Graph")
axe.grid(True)
axe.legend(loc="best")

plt.show()