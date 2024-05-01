from typing import List

def display(matrix: List[List[int]]):
    """
    Display a 2D matrix as a grid of characters.

    Parameters:
    - matrix (List[List[int]]): The 2D matrix to be displayed.

    The function prints each value in the 2D matrix as a character based on its magnitude. If a value is 0, it is printed as a space character (' '). If a value is greater than 0, it is printed as an asterisk character ('*'). 

    Example:
    >>> display([[0, 1, 0], [1, 1, 0], [0, 0, 1]])
     * 
    ** 
      *
    """

    for row in matrix:
        for value in row:
            if value == 0:
                print(' ', end='')
            elif value > 0:
                print('*', end='')
        print('')
    print('')