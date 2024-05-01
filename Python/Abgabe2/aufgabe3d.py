# Wörterbuch mit deutschen und englischen Übersetzungen
woerterbuch = {
    "Haus": "house",
    "Katze": "cat",
    "Auto": "car",
    "Tisch": "table",
    "Apfel": "apple"
}

# Rückwärts-Wörterbuch für die Rückübersetzung
rueckwaerts_woerterbuch = {v: k for k, v in woerterbuch.items()}

def uebersetze_wort(wort):
    if wort in woerterbuch:
        return woerterbuch[wort]
    elif wort in rueckwaerts_woerterbuch:
        return rueckwaerts_woerterbuch[wort]
    else:
        return "Übersetzung nicht gefunden."

def uebersetze_satz(satz):
    uebersetzter_satz = []
    for wort in satz.split():
        uebersetzter_wort = uebersetze_wort(wort)
        if uebersetzter_wort != "Übersetzung nicht gefunden.":
            uebersetzter_satz.append(uebersetzter_wort)
        else:
            return "Nicht alle Wörter im Satz wurden übersetzt."
    return ' '.join(uebersetzter_satz)

# Testen der Funktionen
while True:
    eingabe = input("Geben Sie ein deutsches oder englisches Wort oder einen Satz ein (zum Beenden 'exit' eingeben): ")
    if eingabe.lower() == 'exit':
        break
    if ' ' in eingabe:
        print(uebersetze_satz(eingabe))
    else:
        print(uebersetze_wort(eingabe))
