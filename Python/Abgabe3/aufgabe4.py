from typing import List
from aufgabe3a import create
from aufgabe3c import getNeighbours
from aufgabe3d import display

import time

def nextGeneration(universe: List[List[int]], neighbour: List[List[int]]) -> List[List[int]]:
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

display(matrix)

while True:
    display(matrix)
    neighbour_matrix = getNeighbours(matrix)

    matrix = nextGeneration(matrix, neighbour_matrix)
    
    time.sleep(1)
