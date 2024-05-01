from typing import List

def display(matrix: List[List[int]]):
    for row in matrix:
        for value in row:
            if value == 0:
                print(' ', end='')
            elif value > 0:
                print('*', end='')
        print('')