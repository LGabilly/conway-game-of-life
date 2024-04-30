from models.Pattern import Pattern

PATTERN_DICT: dict[str | None, dict] = {
    "blinker": {
        "pattern": Pattern(name="Blinker", alive_cells={(2, 1), (2, 2), (2, 3)}),
        "bbox": (0, 0, 4, 4),
    },
    "glider_gun": {
        "pattern": Pattern(
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
        "bbox": (0, 0, 40, 10),
    },
}