

eingabe = input("Bitte eine Zahl eingeben:")
while eingabe != "quit":
    try:
        eingabe_complex = complex(eingabe)
        print(eingabe_complex," ist eine komplexe Zahl")

        eingabe_float = round(abs(eingabe_complex), 4)
        print(eingabe_float," ist der Betrag der komplexen Zahl")

        eingabe_int = int(eingabe_float)
        print(eingabe_int," ist der Betrag als Integer")

        eingabe_hex = hex(eingabe_int)
        eingabe_binary = bin(eingabe_int)
        print(eingabe_hex, "ist der Integer in hexadezimaler Darstellung.", eingabe_binary, "ist der Integer als binäre Darstellung")
        eingabe_char = chr(eingabe_int)
        print(eingabe_char," ist der Integer als Schriftzeichen")
    except:
            print("Fehler")
    eingabe = input("Bitte eine Zahl eingeben:")
