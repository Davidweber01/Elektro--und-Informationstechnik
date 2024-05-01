from typing import List
from aufgabe3a import create
from aufgabe3c import getNeighbours
from aufgabe3d import display

import time

def nextGeneration(universe: List[List[int]], neighbour: List[List[int]]) -> List[List[int]]:
    """
    Calculate the next generation of cells in Conway's Game of Life.

    Parameters:
    - universe (List[List[int]]): The current state of the universe (2D matrix of cells).
    - neighbour (List[List[int]]): The number of live neighbors for each cell in the universe.

    Returns:
    - List[List[int]]: The next generation of cells based on the rules of Conway's Game of Life.

    The function iterates over each cell in the universe and determines its state in the next generation based on the number of live neighbors calculated using the neighbour matrix. It applies the rules of Conway's Game of Life to determine whether each cell lives, dies, or becomes alive in the next generation.

    Example:
    >>> nextGeneration([[0, 1, 0], [1, 1, 0], [0, 0, 1]], [[2, 3, 2], [3, 4, 3], [3, 3, 3]])
    [[0, 1, 0], [1, 0, 1], [1, 1, 1]]
    """

    num_rows = len(universe)
    num_cols = len(universe[0]) if universe else 0

    new_universe = [[0] * num_cols for _ in range(num_rows)]
    for row in range(num_rows):
        for col in range(num_cols):
            num_neighbors = neighbour[row][col]
            
            if universe[row][col] == 1:  # Current cell is alive
                if num_neighbors < 2 or num_neighbors > 3:
                    new_universe[row][col] = 0  # Dies due to underpopulation or overpopulation
                else:
                    new_universe[row][col] = 1  # Survives to the next generation
            else:  # Current cell is dead
                if num_neighbors == 3:
                    new_universe[row][col] = 1  # Becomes alive due to reproduction

    return new_universe

matrix = create(10, 10)

while True:
    display(matrix)
    neighbour_matrix = getNeighbours(matrix)
    matrix = nextGeneration(matrix, neighbour_matrix)

    time.sleep(1)
