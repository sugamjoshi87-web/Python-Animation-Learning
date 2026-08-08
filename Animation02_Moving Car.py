import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle, Circle
from matplotlib.animation import FuncAnimation

fig, ax = plt.subplots()

ax.set_xlim(0,20)
ax.set_ylim(0,20)
ax.grid(True)
ax.axhline(y=3.5, linewidth = 3)
ax.axhline(y=7.5, linewidth = 3)

body = Rectangle((0,4), 4, 2, color = "green")
roof = Rectangle((1.5,6), 1.5,1, color = "green")
front_wheel = Circle((1,3.9), 0.3, color = "black")
rear_wheel = Circle((3,3.9), 0.3, color = "black")
window_1 = Rectangle((1,5), 0.5, 0.5, color = "red")
window_2 = Rectangle((3,5), 0.5, 0.5, color = "red")
headlight = Circle((4,5), 0.1, color = "yellow")
tail_light = Circle((0,5), 0.1, color = "red")
truck1 = Rectangle((2,7.5), 0.5, 2, color = "brown")
leaves1 = Circle((2.25, 10), 1.2, color = "green")
truck2 = Rectangle((15,7.5), 0.5, 2, color = "brown")
leaves2 = Circle((15.25,10),1.2,color = "green")

road_line1 = Rectangle((0.5,5.3), 1.5, 0.1, color = "black")
road_line2 = Rectangle((3,5.3), 1.5,0.1, color = "black")
road_line3 = Rectangle((5.5,5.3),1.5,0.1, color = "black")
road_line4 = Rectangle((8,5.3), 1.5, 0.1, color = "black")
road_line5 = Rectangle((10.5,5.3), 1.5, 0.1, color = "black")
road_line6 = Rectangle((13,5.3), 1.5, 0.1, color = "black")
road_line7 = Rectangle((15.5,5.3), 1.5, 0.1, color = "black")
road_line8 = Rectangle((18,5.3), 1.5, 0.1, color = "black")

road_lines = [ road_line1,road_line2,road_line3,road_line4, road_line5, road_line6, road_line7, road_line8]
line_postions = [0.5, 3, 5.5, 8, 10.5, 13, 15.5, 18]

ax.add_patch(body)
ax.add_patch(roof)
ax.add_patch(front_wheel)
ax.add_patch(rear_wheel)
ax.add_patch(window_1)
ax.add_patch(window_2)
ax.add_patch(headlight)
ax.add_patch(tail_light)
ax.add_patch(road_line1)
ax.add_patch(road_line2)
ax.add_patch(road_line3)
ax.add_patch(road_line4)
ax.add_patch(road_line5)
ax.add_patch(road_line6)
ax.add_patch(road_line7)
ax.add_patch(road_line8)
ax.add_patch(truck1)
ax.add_patch(leaves1)
ax.add_patch(truck2)
ax.add_patch(leaves2)

car_x = 0
line_x = 0
tree_x = 0

def update(frame):
    global car_x,line_x,tree_x

    car_x+=0.1
    line_x-=0.1
    tree_x-=0.1

    if car_x > 20:
        car_x = -4

    if line_x < -2.5:
        line_x = 0

    if tree_x < -10:
        tree_x = 20

    body.set_xy((car_x,4))
    roof.set_xy((car_x+1.5,6))
    front_wheel.center = (car_x+1, 3.9)
    rear_wheel.center = (car_x+3, 3.9)
    window_1.set_xy((car_x +1,5))
    window_2.set_xy((car_x+3,5))
    headlight.center = (car_x+4,5)
    tail_light.center = (car_x+0,5)
    for line, start_x in zip(road_lines, line_postions):
        line.set_xy((start_x + line_x, 5.3))

    truck1.set_xy((tree_x+2, 7.5))
    leaves1.center = (tree_x+2.25, 10)
    truck2.set_xy((tree_x+15, 7.5))
    leaves2.center = (tree_x+15.25, 10)

    return body,front_wheel,rear_wheel,roof,window_1,window_2,headlight,tail_light,*road_lines,truck1,leaves1,truck2,leaves2,

ani = FuncAnimation(fig, update, frames=250, interval = 20, blit = True, repeat = False)
plt.show()