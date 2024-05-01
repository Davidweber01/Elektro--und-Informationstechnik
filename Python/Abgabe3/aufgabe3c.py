from typing import List
from aufgabe3b import neighbourCount

def getNeighbours(matrix: List[List[int]]) -> List[List[int]]:
    num_rows = len(matrix)
    num_cols = len(matrix[0]) if matrix else 0 
    return [[neighbourCount(matrix, row, col) for col in range(num_cols)] for row in range(num_rows)]
