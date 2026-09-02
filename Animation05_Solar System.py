import matplotlib.pyplot as plt
import numpy as np
from matplotlib.animation import FuncAnimation

fig, ax = plt.subplots()

def create_sun():
    sun = plt.Circle((0,0), 0.2, color = "yellow")
    ax.add_patch(sun)

    sun_glow = plt.Circle((0,0), 0.27, color="orange", alpha=0.2)
    ax.add_patch(sun_glow)

    return sun,sun_glow

sun,sun_glow = create_sun()

ax.set_title("Solar System Animation", fontsize=16, fontweight="bold")
ax.set_facecolor("black")

def create_moon():
    moon = plt.Circle((1.15, 0), 0.03, color = "gray")
    ax.add_patch(moon)

    moon_orbit = plt.Circle((1,0), 0.15, fill=False)
    ax.add_patch(moon_orbit)

    moon_label = ax.text(1.15, 0, "Moon", fontsize=8, ha="center", va="bottom", color ="white")

    return moon, moon_orbit, moon_label

moon, moon_orbit, moon_label = create_moon()

names = ["Mercury", "Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus", "Neptune"]
radii = [0.7, 0.85, 1.0, 1.5, 2.0, 2.5, 3.0, 3.5]
sizes = [0.05, 0.07, 0.08, 0.06, 0.12, 0.1, 0.09, 0.09]
speeds = [0.08, 0.06, 0.05, 0.03, 0.02, 0.015, 0.01, 0.008]
colors = ["gray","yellow", "blue", "red", "orange", "gold", "lightblue", "darkblue"]

def create_planets():
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

        label = ax.text(radius,0,name,fontsize=9, ha="center", va = "bottom", color ="white")
        labels.append(label)

    return planets,orbits,labels

planets,orbits,labels = create_planets()

def update(frame):

    for planet, radius, speed, label in zip(planets, radii, speeds, labels):

        angle = frame * speed

        x = radius * np.cos(angle)
        y = radius * np.sin(angle)

        planet.center = (x, y)
        label.set_position((x, y))

    earth_angle = frame * speeds[2]

    earth_x = radii[2] * np.cos(earth_angle)
    earth_y = radii[2] * np.sin(earth_angle)

    moon_angle = frame * 0.15

    moon_x = earth_x + 0.15 * np.cos(moon_angle)
    moon_y = earth_y + 0.15 * np.sin(moon_angle)
    moon.center = (moon_x, moon_y)

    moon_orbit.center = (earth_x, earth_y)
    moon_label.set_position((moon_x, moon_y))

    return planets + labels + [moon, moon_orbit, moon_label]

ani = FuncAnimation(fig, update, frames = 500, interval = 20, blit=True)

ax.set_xlim(-4,4)
ax.set_ylim(-4,4)
ax.grid(False)

ax.set_aspect("equal")

plt.show()
