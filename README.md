# RGame – Lightweight 2D Game Engine for Python

**RGame** is a simple, object-oriented 2D game/physics framework built entirely on Python's built-in `tkinter` library. It provides separated physics and rendering loops (running in different threads), precise vector math using `decimal.Decimal`, built-in error handling, and a clean script-based architecture.

Perfect for small educational projects, prototypes, simple games, simulations, or learning how game engines work under the hood.

## Features

- Multithreaded physics (default ~20 Hz) and rendering (~10 Hz) loops
- Precise 2D vector math with `Decimal` (no floating-point errors)
- Easy-to-use appearance system: circles, rectangles, ellipses, lines, labels, images
- Built-in keyboard & mouse input handling
- Error handling & failsafe system (won't crash on first exception)
- Script-based architecture — everything inherits from `RG_Script`
- No external dependencies beyond Python's standard library

## Installation

```bash
# Clone the repository
git clone https://github.com/YOUR-USERNAME/RGame.git
cd RGame

# (optional) Create virtual environment
python -m venv venv
source venv/bin/activate    # Linux/macOS
venv\Scripts\activate       # Windows
```
No pip install is required — just run your scripts!


## Quick Start
Create a file game.pyw (.pyw hides the console):

```python
from RGame import *

class MyGame(RG_MainScript):
    def Main(self):
        # Create a red circle in the center
        self.circle = RG_Circle(
            self,
            position=RG_Position2D(
                self.MainWindow.WindowWidth / 2,
                self.MainWindow.WindowHeight / 2
            ),
            radius=30,
            color="red",
            name="Player"
        )
        
        # Give it some velocity
        self.circle.Velocity = RG_Velocity2D(80, 120)

    def PhysicsTick(self, deltaTime):
        # Bounce off screen edges
        w, h = self.MainWindow.WindowWidth, self.MainWindow.WindowHeight
        r = self.circle.Appearance.Dimensions.Radius
        
        if self.circle.Position.X - r < 0 or self.circle.Position.X + r > w:
            self.circle.Velocity.X *= -1
        if self.circle.Position.Y - r < 0 or self.circle.Position.Y + r > h:
            self.circle.Velocity.Y *= -1

def main():
    return MyGame()

Run(main)
```

Run it:
```bash
python game.pyw
```

