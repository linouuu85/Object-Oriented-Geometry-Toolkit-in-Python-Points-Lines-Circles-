# 📐 Geometric Object Library - Python OOP

A clean implementation of fundamental geometric shapes using **Object-Oriented Programming (OOP)**. This library provides tools to manipulate and analyze spatial relationships between points, lines, and circles in a 2D plane.

## Key Features
- **Point Manipulation**: Define coordinates, translate positions, and calculate Euclidean distances between points.
- **Line Segments**: Create lines from point instances and calculate their exact length.
- **Advanced Circle Logic**:
  - Calculate area and perimeter using the `math` library.
  - **Point Localization**: Determine if a point is inside, outside, or exactly on the circle's edge.
  - **Intersection Logic**: Detect if two circles are secant (intersecting) using the triangle inequality theorem.

## Technical Concepts
- **Composition**: The `Cercle` and `Droite` classes use `Point` objects as attributes, demonstrating the "has-a" relationship in OOP.
- **Encapsulation**: Math operations are encapsulated within class methods (`distance_vers`, `est_secant`) for cleaner code.
- **Special Methods**: Implementation of `__str__` and `__repr__` for professional debugging and object visualization.

## Usage Example
```python
from math import *

# Define a center and a circle
center = Point(0, 0)
my_circle = Cercle(center, 5)

# Check if a point (3, 4) is inside
p = Point(3, 4)
print(my_circle.position_point(p)) # Output: "Sur" (since 3²+4²=5²)
