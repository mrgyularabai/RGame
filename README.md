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

# Available Built-in Shapes in RGame

RGame provides several convenient classes that create visual objects on the screen using Tkinter canvas appearances. All of these classes inherit from `RG_Script` and automatically handle position, velocity, and rendering when added to your `MainScript`.

| Class              | Appearance Type     | Typical Use Case                     | Constructor Example (simplified)                                      |
|--------------------|---------------------|--------------------------------------|-----------------------------------------------------------------------|
| `RG_Circle`        | Circle             | Balls, particles, buttons, icons     | `RG_Circle(self, radius=20, color="red")`                            |
| `RG_Ellipse`       | Ellipse/Oval       | Stretched shapes, eyes, backgrounds  | `RG_Ellipse(self, radiusX=40, radiusY=20, color="blue")`             |
| `RG_Rectangle`     | Rectangle          | Platforms, UI panels, boxes          | `RG_Rectangle(self, width=100, height=60, color="green")`            |
| `RG_Line`          | Line / Polyline    | Trails, debug lines, paths           | `RG_Line(self, points=[p1, p2, p3], color="black", width=3)`         |
| `RG_Label`         | Text Label         | Score display, HUD, instructions     | `RG_Label(self, text="Score: 0", fontSize=24, fontColor="white")`    |
| `RG_Image`         | Image              | Sprites, backgrounds, characters     | `RG_Image(self, fileLocation="assets/player.png")`                   |

### Key Notes
- All constructors accept optional parameters like:
  - `position`: `RG_Position2D(x, y)`
  - `velocity`: `RG_Velocity2D(x, y)`
  - `OffSet`: `RG_Vector2D(x, y)` (for fine-tuning appearance position)
  - `name`: string (useful for debugging)
- The appearance is automatically created and linked via the `appearance` parameter in the base `RG_Script` class.
- Example usage:
  ```python
  self.player = RG_Circle(
      self,
      position=RG_Position2D(100, 100),
      velocity=RG_Velocity2D(50, 0),
      radius=15,
      color="yellow",
      name="PlayerBall"
  )
