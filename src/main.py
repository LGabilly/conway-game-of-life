import random

import click

from models.CursesView import CursesView
from models.Pattern import Pattern

# blinker = Pattern(name="Blinker", alive_cells={(2, 1), (2, 2), (2, 3)})


@click.command()
@click.option("--gen", default=100, show_default=True)
@click.option("--scale", default=10, show_default=True)
@click.option("--pop", default=0.3, show_default=True)
def main(gen: int, scale: int, pop: float):
    random_pattern = Pattern(
        name="Random",
        alive_cells={
            (x, y)
            for x in range(-scale // 2, scale // 2)
            for y in range(-scale // 2, scale // 2)
            if random.random() < pop
        },
    )

    CursesView(
        pattern=random_pattern,
        gen=gen,
        bbox=(-(1.1 * scale), -(1.1 * scale), 1.1 * scale, 1.1 * scale),
    ).show()


if __name__ == "__main__":
    main()
