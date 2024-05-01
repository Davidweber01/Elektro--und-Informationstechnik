import random
from typing import List

def displayListe2D(liste: List[List[int]]):
    """
    Display a 2D list as a grid of characters based on a dictionary mapping values to characters.

    Parameters:
    - liste (List[List[int]]): The 2D list to be displayed.

    The function prints each value in the 2D list as a character according to the mapping defined in the dictionary. If a value is not found in the dictionary, it is replaced with '?'.

    Example:
    >>> displayListe2D([[0, 1, 2, 3], [3, 2, 1, 0]])
    .:.!
    !:?!.
    """

    dictionary = {0: ' ',1: '.', 2: ':', 3: '!'}
    for row in liste:
        for value in row:
            print(dictionary.get(value, '?'), end='')
        print('')

# Define the dimensions of the 2D list
rows = 4
cols = 4

# Create a 2D list filled with integer values from 0 to 3
matrix = [[random.randint(0, 3) for _ in range(cols)] for _ in range(rows)]

for row in matrix:
    print(row)

displayListe2D(matrix)

