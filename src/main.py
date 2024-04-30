import random

from models.CursesView import CursesView
from models.Pattern import Pattern

# blinker = Pattern(name="Blinker", alive_cells={(2, 1), (2, 2), (2, 3)})

random_pattern = Pattern(
    name="Random",
    alive_cells={(x, y) for x in range(10) for y in range(10) if random.random() > 0.3},
)

CursesView(pattern=random_pattern, gen=100, bbox=(-20, -20, 20, 20)).show()
