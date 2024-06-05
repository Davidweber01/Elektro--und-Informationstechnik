from Universum import Universum
from time import sleep

if __name__ == "__main__":
    universum = Universum(50, 50)

    while True:
        print("Nächster Schritt:\n")
        universum.darstellung()
        universum.berechne_folgezustand()
        sleep(1)