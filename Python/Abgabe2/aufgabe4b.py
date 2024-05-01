import random
import numpy as np
import math

liste = []

n = int(input("Geben Sie die Größe der Matrix (N x N) ein: "))

for _ in range(n*n):
    zufallszahl = random.randint(-9, 9)
    liste.append(zufallszahl)

matrix = np.array(liste).reshape(n, n)

print("Matrix:")
print(matrix)

def summe_der_nachbarn(matrix, row, col):
    summe = 0
    for i in range(row-1, row+2):
        for j in range(col-1, col+2):
            # Verwenden der Modulo-Operation, um zyklische Randpositionen zu berücksichtigen
            r = i % n
            c = j % n
            summe += matrix[r][c]
    # Subtrahieren des aktuellen Elements, da es nicht zu den Nachbarn gehört
    summe -= matrix[row][col]
    return summe


while True:
    position = input("Geben Sie die Position in der Form 'row,col' ein oder 'exit' zum Beenden: ")
    if position.lower() == 'exit':
        break
    try:
        row, col = map(int, position.split(','))
        if 0 <= row <= n and 0 < col < n:
            nachbars_summe = summe_der_nachbarn(matrix, row, col)
            print("Summe der Nachbarn an Position ({},{}) ist: {}".format(row, col, nachbars_summe))
        else:
            print("Ungültige Position. Bitte geben Sie eine Position innerhalb der Matrix ein.")
    except ValueError:
        print("Ungültige Eingabe. Bitte geben Sie die Position in der Form 'row,col' ein.")
