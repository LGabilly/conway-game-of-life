import collections

from pydantic import BaseModel

from models.Pattern import Pattern


class LifeGrid(BaseModel):
    pattern: Pattern
    start_col: int = 0
    start_row: int = 0
    end_row: int = 10
    end_col: int = 10

    def evolve(self):
        relative_neighbors_coordinate = (
            (-1, -1),  # North West
            (-1, 0),  # North
            (-1, 1),  # North East
            (0, -1),  # West
            (0, 1),  # East
            (1, -1),  # South West
            (1, 0),  # South
            (1, 1),  # South East
        )
        num_neighbors = collections.defaultdict(int)
        for row, col in self.pattern.alive_cells:
            for relative_row, relative_col in relative_neighbors_coordinate:
                num_neighbors[(row + relative_row, col + relative_col)] += 1

        staying_alive_cells = {
            cell for cell, num in num_neighbors.items() if num in {2, 3}
        }.intersection(self.pattern.alive_cells)

        becomming_alive_cells = {
            cell for cell, num in num_neighbors.items() if num in {3}
        }.difference(self.pattern.alive_cells)

        self.pattern.alive_cells = set.union(staying_alive_cells, becomming_alive_cells)

    def __str__(self):
        return (
            f"{self.pattern.name}:\n"
            f"Alive cells -> {sorted(self.pattern.alive_cells)}"
        )

    def display_ascii(self):
        ALIVE = "💚"
        DEAD = " "

        display = []
        for row in range(self.start_row, self.end_col):
            single_row_display = []
            for col in range(self.start_col, self.end_col):
                single_row_display.append(
                    ALIVE if (row, col) in self.pattern.alive_cells else DEAD
                )
            display.append(" ".join(single_row_display))

        return "\n".join(display)
