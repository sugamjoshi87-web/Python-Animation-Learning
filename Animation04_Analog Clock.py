import matplotlib.pyplot as plt
import numpy as np
from datetime import datetime
from matplotlib.animation import FuncAnimation

fig, ax = plt.subplots()

circle = plt.Circle((0,0), 1.1, fill=False)
ax.add_patch(circle)

for hour in range(12):
    angle =np.pi / 2 - hour * 2 * np.pi / 12
    x =  np.cos(angle)
    y =  np.sin(angle)

    x1 = 1.02 * np.cos(angle)
    y1 = 1.02 * np.sin(angle)

    if hour % 3 == 0:
        inner_radius = 0.90
    else:
        inner_radius = 0.95

    x2 = inner_radius * np.cos(angle)
    y2 = inner_radius * np.sin(angle)

    ax.plot([x1,x2], [y1,y2])
    
    number = 12 if hour == 0 else hour
    ax.text(x,y,str(number),ha ="center", va ="center", fontsize=14,fontweight="bold")

second_hand , = ax.plot([0,0], [0,0], linewidth=1)
minute_hand, = ax.plot([0,0],[0,0], linewidth=3)
hour_hand, = ax.plot([0,0],[0,0], linewidth=5)

center = plt.Circle((0,0), 0.05, color = "black")
ax.add_patch(center)

time_text = ax.text(0, -1.35, "", ha ="center", va="center",fontsize = 14, fontweight="bold")

def update(frame):
    now = datetime.now()

    second_angle = np.pi / 2 - 2 * np.pi * now.second / 60
    minute_angle = np.pi / 2 - 2* np.pi * (now.minute + now.second / 60) / 60
    hour_angle = np.pi / 2 - 2 * np.pi * (now.hour + now.minute / 60) / 12

    x_second = 0.85 * np.cos(second_angle)
    y_second = 0.85 * np.sin(second_angle)

    x_minute = 0.70 * np.cos(minute_angle)
    y_minute = 0.70 * np.sin(minute_angle)

    x_hour = 0.55 * np.cos(hour_angle)
    y_hour = 0.55 * np.sin(hour_angle)

    second_hand.set_data([0,x_second], [0,y_second])
    minute_hand.set_data([0,x_minute],[0,y_minute])
    hour_hand.set_data([0,x_hour],[0,y_hour])

    time_text.set_text(now.strftime("%H:%M:%S"))

    return second_hand,minute_hand,hour_hand,time_text

ani = FuncAnimation(fig, update, interval = 1000, blit=True)

ax.set_xlim(-1.5, 1.5)
ax.set_ylim(-1.5, 1.5)

ax.set_aspect("equal")
ax.grid(False)

plt.show()