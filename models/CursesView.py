import curses
from time import sleep

from pydantic import BaseModel

from models.LifeGrid import LifeGrid
from models.Pattern import Pattern


class CursesView(BaseModel):
    pattern: Pattern
    gen: int = 10
    frame_rate: int = 6
    bbox: tuple = (0, 0, 10, 10)

    def show(self):
        curses.wrapper(self._draw)

    def _draw(self, screen):
        current_grid = LifeGrid(
            pattern=self.pattern,
            start_col=self.bbox[0],
            start_row=self.bbox[1],
            end_col=self.bbox[2],
            end_row=self.bbox[3],
        )
        curses.curs_set(0)
        screen.clear()

        try:
            screen.addstr(0, 0, current_grid.display_ascii())
        except curses.error:
            raise ValueError(
                f"Error: terminal too small for pattern '{self.pattern.name}'"
            )

        for _ in range(self.gen):
            current_grid.evolve()
            screen.addstr(0, 0, current_grid.display_ascii())
            screen.refresh()
            sleep(1 / self.frame_rate)
