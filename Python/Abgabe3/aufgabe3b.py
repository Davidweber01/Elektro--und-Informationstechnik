from typing import List

def neighbourCount(matrix: List[List[int]], row, col) -> int:
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