from src.grid.grid import BasicGrid
from src.grid.structure import GridStructure


class Food(GridStructure):
    """
        Manage a food on the grid.
    """

    def __init__(self, grid: BasicGrid, color: tuple):
        super().__init__(grid, [grid.get_cell(7, 0)], color)
