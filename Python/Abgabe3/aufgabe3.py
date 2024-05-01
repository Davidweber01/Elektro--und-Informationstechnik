from aufgabe3a import create
from aufgabe3c import getNeighbours
from aufgabe3d import display

matrix = create(3, 4)
for row in matrix:
    print(row)

print('')

display(matrix)


neighbour_matrix = getNeighbours(matrix)

for row in neighbour_matrix:
    print(row)

