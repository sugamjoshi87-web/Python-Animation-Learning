# Python Animation Learning 

## 📖 About This Journey

This repository documents my journey of learning **Python Animation with Matplotlib** through practical projects.

Instead of learning only from theory, I am building small animations step by step to understand how Python, NumPy, Matplotlib, mathematics, and animation logic work together.

This repository is also intended to be useful for **beginners who want to learn Matplotlib Animation by following a practical project-based approach.**

The projects gradually become more complex, allowing each project to build on concepts learned in the previous one.

## 🛣️ Learning Roadmap

The projects are arranged from simple to more complex concepts:

| Project                      | Main Focus                            |
| ---------------------------- | ------------------------------------- |
| 🟢 Project 1 – Bouncing Ball | Basic animation and `FuncAnimation()` |
| 🚗 Project 2 – Moving Car    | Multiple Artists and object movement  |
| 🌊 Project 3 – Sine Wave     | NumPy and mathematical animation      |
| 🕐 Project 4 – Analog Clock  | Angles and circular motion            |
| 🌍 Project 5 – Solar System  | Multiple objects and relative motion  |

### Recommended Path

**Bouncing Ball → Moving Car → Sine Wave → Analog Clock → Solar System**

Beginners are encouraged to follow the projects in order because each project introduces concepts that are useful in later projects.


##  Project 1: Bouncing Ball Animation

A simple bouncing ball animation created using Python and Matplotlib.

### Concepts Learned

* `FuncAnimation`
* Figure and Axes
* Artists
* `update(frame)`
* Position `(x, y)`
* Velocity `(dx, dy)`
* Collision detection
* `blit=True`
* Animation frames and intervals

### Technologies

* Python
* Matplotlib

### File

```text
Animation01_BouncingBall.py
```

---

## 🚗 Project 2: Moving Car Animation

A moving car animation created using **Matplotlib patches and FuncAnimation**.

The scene contains a moving car, road markings, and trees. The project helped me understand how multiple Matplotlib Artists can be updated together.

### Features

* 🚗 Moving car
* 🛞 Two wheels
* 🏠 Car roof
* 🪟 Windows
* 💡 Headlight
* 🔴 Tail light
* 🛣️ Moving road markings
* 🌳 Multiple moving trees
* 🔄 Continuous movement
* 🎬 Frame-based animation

### Concepts Learned

* `FuncAnimation`
* `Rectangle`
* `Circle`
* Matplotlib Patches
* Matplotlib Artists
* `set_xy()`
* `.center`
* Position variables
* Lists
* `zip()`
* Loops
* `global` variables
* Continuous movement
* Object resetting
* `blit=True`

### Technologies

* Python
* Matplotlib

### File

```text
Animation02_Moving_Car.py
```

---

### 🌊 Project 3: Interactive Sine Wave Animation

An interactive sine wave animation created using Python, NumPy, and Matplotlib.

The project started with a basic animated sine wave and was gradually developed by adding amplitude, frequency, phase, offset, and keyboard interaction.

### Features
🌊 Animated sine wave

📈 Adjustable amplitude

🔄 Adjustable frequency

⏯️ Pause and resume animation

🔁 Reset functionality

🖱️ Mouse interaction

🎬 Frame-based animation

⚡ Smooth animation using blit=True

### 🎮 Keyboard Controls

| Key | Action |
|---|---|
| ⬆️ Up Arrow | Increase amplitude |
| ⬇️ Down Arrow | Decrease amplitude |
| ➡️ Right Arrow | Increase frequency |
| ⬅️ Left Arrow | Decrease frequency |
| `SPACE` | Pause / Resume animation |
| `R` | Reset animation parameters |

### Mathematical Model

The sine wave is represented by:

y = A sin(Bx + φ) + C

Where:

A = Amplitude

B = Frequency

φ = Phase

C = Vertical Offset

### Concepts Learned

* NumPy arrays
* np.linspace()
* np.sin()
* Mathematical functions
* Sine waves
* Amplitude
* Frequency
* Phase
* Offset
* FuncAnimation
* update(frame)
* init_func
* blit=True
* Keyboard events
* Mouse events
* mpl_connect()
* Interactive visualization
* Program state management

### Technologies

* Python
* NumPy
* Matplotlib

 ### File

```text
Animation03_Interactive_Sine_Wave.py
```

---

## 🕐 Project 4: Real-Time Analog Clock

A real-time analog clock created using **Python, NumPy, Matplotlib, and the datetime module**.

The project started with a basic clock face and was gradually developed by adding clock numbers, tick marks, animated hour, minute, and second hands, a center pin, and a digital time display.

### Features

* 🕐 Real-time analog clock
* 🔢 12 clock numbers
*  |  Hour, minute, and second tick marks`
* ⏱️ Animated second hand
* 🕒 Animated minute hand
* 🕰️ Animated hour hand
* ⚫ Center pin
* 🖥️ Digital `HH:MM:SS` time display
* 🔄 Real-time updates
* ⚡ Smooth animation using `blit=True`

### Concepts Learned

* `datetime.now()`
* `FuncAnimation`
* `update(frame)`
* Matplotlib Line Artists
* Matplotlib Text Artists
* Matplotlib Circle
* `set_data()`
* `set_text()`
* `np.sin()`
* `np.cos()`
* `np.pi`
* Radians
* Angle calculation
* Coordinate systems
* Converting angles into `(x, y)` coordinates
* Updating multiple Artists
* Real-time animation
* `blit=True`

### Mathematical Concept

The position of each clock hand is calculated using:

```text
x = r × cos(angle)
y = r × sin(angle)

The clock converts:

60 seconds → one full rotation
60 minutes → one full rotation
12 hours   → one full rotation
The hour and minute calculations also include fractional time so that the hands move naturally between the clock numbers.
```

### Technologies

* Python
* NumPy
* Matplotlib
* datetime

### File

```
`Animation04_Analog_Clock.py`
```

### 5. 🌍 Solar System Animation

A solar system animation created using **Python and Matplotlib**, demonstrating planetary orbital motion and the Moon's movement around Earth.

## Features:

* ☀️ Sun with a simple glow effect
* 🪐 Planetary orbits
* 🌍 Multiple planets with different orbital radii and speeds
* 🌙 Moon orbiting around Earth
* 🏷️ Labels for planets and Moon
* 🔄 Continuous frame-by-frame animation

## Concepts practiced:

* `FuncAnimation()`
* `update(frame)`
* Matplotlib `Circle` Patches
* Matplotlib Artists
* `np.sin()` and `np.cos()`
* Circular motion
* Lists and `zip()`
* Functions for organizing code
* Updating Artist positions
* Relative motion
* `blit=True`

## Main learning:
This project helped me understand how multiple moving objects can be managed together in an animation. I learned how to calculate circular motion using sine and cosine and how to make the Moon follow Earth's changing position.

The planetary distances and speeds are simplified for visualization and learning purposes rather than representing real astronomical scales.

## Technologies:

* Python
* NumPy
* Matplotlib

## File

```
`Animation05_Solar System.py`
```

## 🧠 Core Concepts Learned

Throughout these projects, I have practiced:

### Python

* Variables
* Lists
* Loops
* Functions
* `zip()`
* Basic program structure

### NumPy

* `np.linspace()`
* `np.sin()`
* `np.cos()`
* Mathematical calculations

### Matplotlib

* Figures and Axes
* Artists
* Patches
* `Circle`
* `Rectangle`
* Text labels
* Updating object positions

### Animation

* `FuncAnimation()`
* `update(frame)`
* Frames
* Animation intervals
* `blit=True`
* Continuous movement
* Circular motion
* Relative motion

### Tools

* VS Code
* Git
* GitHub

## 🎯 How Beginners Can Use This Repository

If you are new to Matplotlib Animation, I recommend following the projects in order.

For each project:

1. Read the project description.
2. Run the code yourself.
3. Read the code line by line.
4. Understand what each function does.
5. Change values and observe the result.
6. Try modifying the animation.
7. Build your own version.

Don't focus only on copying the code. Try to understand **why each part of the code is needed**.

The goal is to learn by experimenting, making mistakes, fixing them, and gradually building more complex animations.

## 🛠️ Technologies Used

- Python
- NumPy
- Matplotlib
- Matplotlib Animation
- VS Code
- Git
- GitHub

---

## 🚀 Future Improvements

I plan to gradually make these animation projects more advanced by adding:

* 🎮 More interactive controls and user input
* 🎬 More complex animations and simulations
* ⚙️ Physics-based movement and interactions
* 📡 Real-time data integration
* 🖱️ Keyboard and mouse controls
* ⚡ Improved animation performance
* 🧩 Better use of Matplotlib Artists and Patches
* 💾 Video and GIF export
* 🔧 More reusable code using functions and classes
* 🏗️ Object-oriented programming for larger projects
* 📁 Better project structure and code organization
* 📐 More advanced mathematical visualizations
* 🔬 Interactive simulations
* 🌌 Advanced projects such as physics simulations
* 📊 Exploring other Python visualization and animation libraries

The main goal is to keep learning by building, making each project more challenging than the previous one.
---

## 📚 My Learning Progress

| Project   | Topic                   | Status      |
| --------- | ----------------------- | ----------- |
| Project 1 | Bouncing Ball Animation | ✅ Completed |
| Project 2 | Moving Car Animation    | ✅ Completed |
| Project 3 | Sine Wave Animation     | ✅  Completed |
| Project 4 | Analog Clock            | ✅ Completed |
| Project 5 | Solar System            | ✅ Completed|

---

## 👨‍💻 Author

**Sugam Joshi**

Computer Engineering Student

---

⭐ This repository is part of my journey to improve my **Python programming and visualization skills through practical projects**.
