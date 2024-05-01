from typing import List
from aufgabe3b import neighbourCount

def getNeighbours(matrix: List[List[int]]) -> List[List[int]]:
    """
    Generate a 2D matrix representing the number of live neighbors for each cell in a given matrix.

    Parameters:
    - matrix (List[List[int]]): The 2D matrix representing the game board.

    Returns:
    - List[List[int]]: A 2D matrix where each cell contains the number of live neighbors for the corresponding cell in the input matrix.

    The function iterates over each cell in the input matrix and calculates the number of live neighbors for each cell using the neighbourCount function. It constructs a new 2D matrix where each cell contains the count of live neighbors for the corresponding cell in the input matrix.

    Example:
    >>> getNeighbours([[0, 1, 0], [1, 1, 0], [0, 0, 1]])
    [[4, 3, 4], [3, 3, 4], [4, 4, 3]]
    """

    num_rows = len(matrix)
    num_cols = len(matrix[0]) if matrix else 0 
    return [[neighbourCount(matrix, row, col) for col in range(num_cols)] for row in range(num_rows)]
