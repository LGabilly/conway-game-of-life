import random

import click

from models.CursesView import CursesView
from models.Pattern import Pattern

PATTERN_DICT: dict[str | None, Pattern] = {
    "blinker": Pattern(name="Blinker", alive_cells={(2, 1), (2, 2), (2, 3)}),
    "glider_gun": Pattern(
        name="Glider gun",
        alive_cells={
            (0, 24),
            (1, 22),
            (1, 24),
            (2, 12),
            (2, 13),
            (2, 20),
            (2, 21),
            (2, 34),
            (2, 35),
            (3, 11),
            (3, 15),
            (3, 20),
            (3, 21),
            (3, 34),
            (3, 35),
            (4, 0),
            (4, 1),
            (4, 10),
            (4, 16),
            (4, 20),
            (4, 21),
            (5, 0),
            (5, 1),
            (5, 10),
            (5, 14),
            (5, 16),
            (5, 17),
            (5, 22),
            (5, 24),
            (6, 10),
            (6, 16),
            (6, 24),
            (7, 11),
            (7, 15),
            (8, 12),
            (8, 13),
        },
    ),
}


@click.command()
@click.option("--gen", default=100, show_default=True)
@click.option("--scale", default=10, show_default=True)
@click.option("--pop", default=0.3, show_default=True)
@click.option("--pattern_name")
def main(gen: int, scale: int, pop: float, pattern_name: str | None):
    if pattern_name:
        pattern = PATTERN_DICT.get(pattern_name)
        if pattern is None:
            raise ValueError(f"{pattern_name=} doesn't not currently exist")
    else:
        pattern = Pattern(
            name="Random",
            alive_cells={
                (x, y)
                for x in range(-scale // 2, scale // 2)
                for y in range(-scale // 2, scale // 2)
                if random.random() < pop
            },
        )

    CursesView(
        pattern=pattern,
        gen=gen,
        bbox=(-(1.1 * scale), -(1.1 * scale), 1.1 * scale, 1.1 * scale),
    ).show()


if __name__ == "__main__":
    main()
