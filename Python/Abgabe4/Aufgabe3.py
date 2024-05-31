from Universum import Universum
from time import sleep

if __name__ == "__main__":
    universum = Universum(50, 50)

    while True:
        universum.darstellung()
        universum.berechne_folgezustand()
        print("Nächster Schritt:\n")
        sleep(1)