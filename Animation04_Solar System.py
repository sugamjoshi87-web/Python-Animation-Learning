import matplotlib.pyplot as plt
import numpy as np
from matplotlib.animation import FuncAnimation

fig, ax = plt.subplots()

sun = plt.Circle((0,0), 0.2, color = "yellow")
ax.add_patch(sun)

names = ["Mercury", "Earth", "Mars", "Jupiter"]
radii = [0.7, 1.0, 1.5, 2.0]
sizes = [0.05, 0.08, 0.06, 0.12]
speeds = [0.08, 0.05, 0.03, 0.02]
colors = ["gray", "blue", "red", "orange"]

planets = []
orbits = []
labels = []

for radius, size, color, name in zip(radii, sizes, colors, names):

    orbit = plt.Circle((0,0), radius, fill = False)
    ax.add_patch(orbit)
    orbits.append(orbit)

    planet = plt.Circle((radius, 0), size, color = color)
    ax.add_patch(planet)
    planets.append(planet)

    label = ax.text(radius,0,name,fontsize=9, ha="center", va = "bottom")
    labels.append(label)

def update(frame):

    for planet, radius, speed, label in zip(planets, radii, speeds, labels):

        angle = frame * speed

        x = radius * np.cos(angle)
        y = radius * np.sin(angle)

        planet.center = (x, y)
        label.set_position((x, y))

    return planets + labels

ani = FuncAnimation(fig, update, frames = 500, interval = 20, blit=True)

ax.set_xlim(-3,3)
ax.set_ylim(-3,3)
ax.grid(True)

ax.set_aspect("equal")

plt.show()
