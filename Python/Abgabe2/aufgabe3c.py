liste = [0]
liste.append([1, 2, 3])
liste.extend([1, 2, 3])
liste.remove([1, 2, 3])
rListe = liste
cListe = liste.copy()
liste.insert(0, -3)
liste.insert(0, -2)
liste.insert(0, -3)
liste.pop(liste.index(0))
print(liste)
print(rListe)
print(cListe)
liste.clear()
print(liste)
print(rListe)
print(cListe)
# liste und rListe beziehen sich auf die selbe Liste, während cListe eine eigene ist