import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import numpy as np

fig, ax= plt.subplots()

x = np.linspace(0, 2*np.pi, 100)
phase = 0
base_amplitude = 3
base_frequency = 2
Offset = 0
y = base_amplitude * np.sin(base_frequency * x + phase) + Offset

line, = ax.plot(x,y)

ax.set_xlim(0, 2*np.pi)
ax.set_ylim(-6, 6)
ax.axhline(y = 0, linewidth = 1, color = "red")
ax.grid(True)

def init():
    line.set_data([],[])
    return line,

def update(frame):
    global phase
    phase+=0.1 
    current_offset = 2 * np.sin(frame * 0.03)
    y =base_amplitude* np.sin(base_frequency * x + phase) + current_offset
    line.set_data(x,y)
    return line,

paused = False


def on_key(event):
    global base_amplitude, base_frequency,paused

    if event.key == "up":
        base_amplitude += 0.2

    elif event.key == "down":
        base_amplitude -= 0.2

    elif event.key == "right":
        base_frequency += 0.1

    elif event.key == "left":
        base_frequency -= 0.1

    elif event.key == " ":
        paused = not paused

        if paused:
            ani.pause()

        else:
            ani.resume()

    elif event.key == "r":
        base_amplitude = 3
        base_frequency = 2
        phase = 0
        Offset = 0

    if base_amplitude < 0:
        base_amplitude = 0

    if base_frequency < 0:
        base_frequency = 0

fig.canvas.mpl_connect("key_press_event", on_key)

def on_click(event):
    print("Mouse clicked")
    print("x=", event.xdata)
    print("y=", event.ydata)

fig.canvas.mpl_connect("button_press_event", on_click)

ani = FuncAnimation(fig, update,init_func=init, frames=200, interval = 20, blit = True)
plt.show()