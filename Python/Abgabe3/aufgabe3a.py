import random
from typing import List

def create(rows: int, *cols: int) -> List[List[int]]:
    """
    Create a 2D array with the specified number of rows and columns, filled with random integers (0 or 1).

    Parameters:
    - rows (int): The number of rows in the 2D array.
    - cols (int, optional): The number of columns in the 2D array. If not provided, the number of columns is equal to the number of rows.

    Returns:
    List[List[int]]: A 2D array with random integers (0 or 1), where each row has the specified number of columns.

    Example:
    >>> create(3, 4)
    [[0, 0, 0, 1], [0, 1, 1, 0], [1, 1, 0, 1]]
    >>> create(2)
    [[0, 1], [1, 0]]
    """
    if not cols:
        cols = rows
    else:
        cols = cols[0]
    print("rows: ", rows, "cols: ", cols)
    return [[random.randint(0, 1) for _ in range(cols)] for _ in range(rows)]

