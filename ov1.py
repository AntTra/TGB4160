import matplotlib.pyplot as plt

# (deposition age, present depth)
units = {
    "Jurassic": (210, 5200),
    "Lower Cretaceous": (140, 4148),
    "Upper Cretaceous": (95, 3689),
    "Paleocene": (65, 2721),
    "Eocene & Younger": (55, 2116),
}

fig, ax = plt.subplots(figsize=(9,6))

for name, (age, depth) in units.items():
    ax.plot([age, 0], [0, depth], marker="o", label=name)

ax.axvspan(140, 160, color="red", alpha=0.2, label="Unconformity (notice 20 myr missing)")

# Geology conventions
ax.invert_yaxis()
ax.set_xlim(210, 0) 

ax.set_xlabel("Geologic Time (Ma)")
ax.set_ylabel("Burial Depth (m)")
ax.set_title("Exercise 1A: Burial History Graph")
ax.grid(True)
ax.legend(loc="best")

############################################################################################

unit = {
    "Pliocene": (5, 650),
    "Miocene": (23, 990),
    "Oliogocene": (36, 1170),
    "Eocene": (57, 1750),
    "Palaeocene": (66, 1940),
    "Upper Cretaceous": (97, 2390),
    "Middle Jurassic": (187, 2560),
    "Lower Jurassic": (208, 2770),
    "Upper Triassic": (230, 2930),
    "Lower Triassic": (245, 3250),
}

figu, axe = plt.subplots(figsize=(9,6))

for name, (age, depth) in unit.items():
    axe.plot([age, 0], [0, depth], marker="o", label=name)

axe.axvspan(187, 97, color="red", alpha=0.2, label="Uplift causing erosion of layers during this period")

# Geology conventions
axe.invert_yaxis()
axe.set_xlim(245, 0) 

axe.set_xlabel("Geologic Time (Ma)")
axe.set_ylabel("Burial Depth (m)")
axe.set_title("Exercise 2A: Burial History Graph")
axe.grid(True)
axe.legend(loc="best")

plt.show()