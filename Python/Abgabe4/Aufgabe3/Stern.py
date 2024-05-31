from random import randint

class Stern:
    def __init__(self):
        self.helligkeit = randint(0, 1)
        self.nachbarn = [None] * 8
        self.lebende_nachbarn = 0

    def __str__(self):
        if self.helligkeit == 0:
            return ' '
        elif self.helligkeit == 1:
            return '*'

    def change_nachbarn(self, list):
        self.nachbarn = list
        self.lebende_nachbarn()

    def lebende_nachbarn(self):
        anzahl_lebender_nachbarn = 0
        for nachbar in self.nachbarn:
            if nachbar != None:
                if nachbar.helligkeit == 1:
                    anzahl_lebender_nachbarn += 1
        self.lebende_nachbarn = anzahl_lebender_nachbarn
        return anzahl_lebender_nachbarn

    def will_survive(self) -> bool:
        

if __name__ == "__main__":
    stern = Stern()
    print(stern)
