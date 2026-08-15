# Python Animation Learning 

This repository documents my journey of learning **Python animation using Matplotlib** through small hands-on projects.

The goal is to understand animation concepts by building projects from scratch and gradually adding more features.


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

## 📚 My Learning Progress

| Project   | Topic                   | Status      |
| --------- | ----------------------- | ----------- |
| Project 1 | Bouncing Ball Animation | ✅ Completed |
| Project 2 | Moving Car Animation    | ✅ Completed |
| Project 3 | Sine Wave Animation     | ✅  Completed |
| Project 4 | Analog Clock            | 🔜 Upcoming |
| Project 5 | Solar System            | 🔜 Upcoming |

---

## 🚀 Future Improvements

I plan to gradually make these animations more advanced by adding:

* 🌞 Sun and clouds
* 🌙 Day/night mode
* 🚦 Traffic lights
* 🚙 Multiple vehicles
* 🏔️ Mountains and buildings
* 💡 Animated headlights
* 🎵 Background sound
* 🎬 Video export
* ⚡ More efficient code using functions and classes

---

## 🧠 What I'm Practicing

Through these projects, I am improving my understanding of:

* Python programming
* Functions
* Loops
* Lists
* Variables
* Object movement
* Animation logic
* Matplotlib
* Problem solving
* Writing cleaner and reusable code

---

## 👨‍💻 Author

**Sugam Joshi**

Computer Engineering Student

---

⭐ This repository is part of my journey to improve my **Python programming and visualization skills through practical projects**.
