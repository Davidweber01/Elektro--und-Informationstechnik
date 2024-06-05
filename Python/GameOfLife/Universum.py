from Stern import Stern
class Universum:
    def __init__(self, zeilen, spalten):
        self.zeilen = zeilen
        self.spalten = spalten
        self.grid = [[Stern() for _ in range(spalten)] for _ in range(zeilen)]
        self.setze_nachbarn()

    def setze_nachbarn(self):
        for i in range(self.zeilen):
            for j in range(self.spalten):
                nachbarn = []
                for di in [-1, 0, 1]:
                    for dj in [-1, 0, 1]:
                        if di == 0 and dj == 0:
                            continue
                        ni, nj = i + di, j + dj
                        if 0 <= ni < self.zeilen and 0 <= nj < self.spalten:
                            nachbarn.append(self.grid[ni][nj])
                        else:
                            nachbarn.append(None)
                self.grid[i][j].change_nachbarn(nachbarn)

    def darstellung(self):
        for x, reihe in enumerate(self.grid):
            for y, stern in enumerate(reihe):
                stern.update(x, y)
            

    def berechne_folgezustand(self):
        for reihe in self.grid:
            for stern in reihe:
                stern.update_lebende_nachbarn()
        
        neue_helligkeit = [[stern.next_gen() for stern in reihe] for reihe in self.grid]
        
        for i in range(self.zeilen):
            for j in range(self.spalten):
                self.grid[i][j].helligkeit = 1 if neue_helligkeit[i][j] else 0

if __name__ == "__main__":
    universum = Universum(5, 5)
    universum.darstellung()
    print("\nNach einem Schritt:\n")
    universum.berechne_folgezustand()
    universum.darstellung()