from models.CursesView import CursesView
from models.Pattern import Pattern

blinker = Pattern(name="Blinker", alive_cells={(2, 1), (2, 2), (2, 3)})

CursesView(pattern=blinker, gen=100, bbox=(0, 0, 10, 10)).show()
