import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

fig, ax = plt.subplots()

ball , = ax.plot([],[], "bo", markersize = 20)

ax.set_xlim(-20,20)
ax.set_ylim(-20,20)

ax.axhline(0, color = "Red")
ax.axvline(0, color = "Red")

x= 0
y = 0
dx = 0.5
dy = 0.34

ax.grid(True)

def update(frame):
    global x,y,dx,dy
    x+=dx
    y+=dy

    if x>=20 or x<=-20:
        dx = -dx
    if y>=20 or y<= -20:
        dy = -dy

    ball.set_data([x], [y])
    return ball,

ani = FuncAnimation(fig, update, frames=500, interval = 30, blit = True, repeat = False)
plt.show()
