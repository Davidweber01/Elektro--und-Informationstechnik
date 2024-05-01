import random

def displayListe2D(liste):
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

