import math

def schnittRadius(radius=1, winkel=90):
    a = radius * math.sin(math.radians(abs(winkel) % 180))
    return a

def schnittHoehe(radius=1, winkel=90):
    h = radius * (1 - math.cos(math.radians(abs(winkel) % 180)))
    return h

def schnittFlaeche(radius=1, winkel=90):
    a = schnittRadius(radius, winkel)
    return math.pi * pow(a, 2)

def oberesTeilVolumen(radius=1, winkel=90):
    h = schnittHoehe(radius, winkel)
    return math.pi / 3 * math.pow(h, 2) * (3 * radius - h)

def unteresTeilVolumen(radius=1, winkel=90):
    h = schnittHoehe(radius, winkel)
    return math.pi / 3 * math.pow(radius - h, 2) * (3 * radius - (radius - h))

def obereMantelflaeche(radius=1, winkel=90):
    a = schnittRadius(radius, winkel)
    return 2 * math.pi * radius * a

def untereMantelflaeche(radius=1, winkel=90):
    a = schnittRadius(radius, winkel)
    return 2 * math.pi * (radius - a)

def teilVolumen(radius=1, winkel=90):
    if winkel == 180:
        return 4/3 * math.pi * math.pow(radius, 3)
    else:
        return oberesTeilVolumen(radius, winkel) + unteresTeilVolumen(radius, winkel)

print(teilVolumen(winkel=180))
print(obereMantelflaeche(winkel=180))
print(untereMantelflaeche(winkel=180))
