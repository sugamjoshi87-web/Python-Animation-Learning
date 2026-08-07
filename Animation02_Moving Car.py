import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle, Circle
from matplotlib.animation import FuncAnimation

fig, ax = plt.subplots()

ax.set_xlim(0,20)
ax.set_ylim(0,20)
ax.grid(True)

body = Rectangle((0,4), 4, 2, color = "blue")
roof = Rectangle((1.5,6), 1.5,1, color = "Red")
front_wheel = Circle((1,3.9), 0.3, color = "black")
rear_wheel = Circle((3,3.9), 0.3, color = "black")

ax.add_patch(body)
ax.add_patch(roof)
ax.add_patch(front_wheel)
ax.add_patch(rear_wheel)

car_x = 0

def update(frame):
    global car_x
    car_x+=0.1
    body.set_xy((car_x,4))
    roof.set_xy((car_x+1.5,6))
    front_wheel.center = (car_x+1, 3.9)
    rear_wheel.center = (car_x+3, 3.9)
    return body,front_wheel,rear_wheel,roof,

ani = FuncAnimation(fig, update, frames=150, interval = 20, blit = True, repeat = False)
plt.show()