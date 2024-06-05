from random import randint
from OpenGL.GL import *

class Stern:
    def __init__(self):
        self.helligkeit = randint(0, 1)
        self.nachbarn = [None] * 8
        self.lebende_nachbarn = 0

    def __str__(self):
        return '*' if self.helligkeit == 1 else ' '

    def change_nachbarn(self, list):
        self.nachbarn = list
        self.update_lebende_nachbarn()

    def update_lebende_nachbarn(self):
        anzahl_lebender_nachbarn = 0
        for nachbar in self.nachbarn:
            if nachbar and nachbar.helligkeit == 1:
                anzahl_lebender_nachbarn += 1
        self.lebende_nachbarn = anzahl_lebender_nachbarn
        return anzahl_lebender_nachbarn

    def next_gen(self) -> bool:
        if self.helligkeit == 1:
            # Live cell rules
            if self.lebende_nachbarn < 2:
                return False  # Dies by underpopulation
            elif 2 <= self.lebende_nachbarn <= 3:
                return True   # Lives on to the next generation
            else:
                return False  # Dies by overpopulation
        else:
            # Dead cell rules
            if self.lebende_nachbarn == 3:
                return True  # Becomes a live cell by reproduction
            else:
                return False # Stays dead

    def update(self, x, y):
        if self.helligkeit == 1:
            glColor3f(1.0, 1.0, 1.0)  # White color for live cells
            glBegin(GL_QUADS)
            glVertex2f(x, y)
            glVertex2f(x + 1, y)
            glVertex2f(x + 1, y + 1)
            glVertex2f(x, y + 1)
            glEnd()
        else:
            glColor3f(1.0, 1.0, 1.0)  # White color for the outline
            glBegin(GL_LINE_LOOP)
            glVertex2f(x, y)
            glVertex2f(x + 1, y)
            glVertex2f(x + 1, y + 1)
            glVertex2f(x, y + 1)
            glEnd()

            

if __name__ == "__main__":
    stern = Stern()
    print(stern)
