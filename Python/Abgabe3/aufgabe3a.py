import random
from typing import List

def create(rows, *cols) -> List[List[int]]:
    if not cols:
        cols = rows
    else:
        cols = cols[0]
    print("rows: ", rows, "cols: ", cols)
    return [[random.randint(0, 1) for _ in range(cols)] for _ in range(rows)]

