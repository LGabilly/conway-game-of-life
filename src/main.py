import random

import click

from models.CursesView import CursesView
from models.Pattern import Pattern
from src.core.pattern_dict import PATTERN_DICT


@click.command()
@click.option("--gen", default=100, show_default=True)
@click.option("--scale", default=10, show_default=True)
@click.option("--pop", default=0.3, show_default=True)
@click.option("--pattern_name")
def main(gen: int, scale: int, pop: float, pattern_name: str | None):
    if pattern_name:
        pattern_as_dict = PATTERN_DICT.get(pattern_name)
        if pattern_as_dict is None:
            raise ValueError(f"{pattern_name=} doesn't not currently exist")
        pattern: Pattern = pattern_as_dict["pattern"]
        bbox: tuple = pattern_as_dict["bbox"]
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
        bbox = (
            round(-1.3 * scale),
            round(-1.3 * scale),
            round(1.3 * scale),
            round(1.3 * scale),
        )

    CursesView(
        pattern=pattern,
        gen=gen,
        bbox=bbox,
    ).show()


if __name__ == "__main__":
    main()
