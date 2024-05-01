from typing import List

def neighbourCount(matrix: List[List[int]], row, col) -> int:
    """
    Count the number of live neighbors for a cell in a 2D matrix.

    Parameters:
    - matrix (List[List[int]]): The 2D matrix representing the game board.
    - row (int): The row index of the cell.
    - col (int): The column index of the cell.

    Returns:
    - int: The number of live neighbors for the specified cell.

    The function calculates the number of live neighbors for a cell at the given row and column indices in the 2D matrix. 
    It considers cells in a 3x3 neighborhood around the specified cell, applying cyclic boundary conditions to handle edge cases.

    Example:
    >>> neighbourCount([[0, 1, 0], [1, 1, 0], [0, 0, 1]], 1, 1)
    3
    """

    num_rows = len(matrix)
    num_cols = len(matrix[0]) if matrix else 0 
    sum = 0
    for i in range(row-1, row+2):
        for j in range(row-1, row+2):
            r = i % num_rows
            c = j % num_cols
            sum += matrix[r][c]
    sum -= matrix[row][col]
    return sum