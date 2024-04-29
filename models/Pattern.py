from pydantic import BaseModel


class Pattern(BaseModel):
    name: str
    alive_cells: set[tuple[int, int]]
