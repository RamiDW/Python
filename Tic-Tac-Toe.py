def spielfeld_anzeigen(spielfeld):
    for reihe in spielfeld:
        print("|".join(reihe))
        print("-" * 5)

def pruefe_gewinner(spielfeld, spieler):
    for reihe in spielfeld:
        if all([feld == spieler for feld in reihe]):
            return True

    for spalte in range(3):
        if all([spielfeld[reihe][spalte] == spieler for reihe in range(3)]):
            return True

    if all([spielfeld[i][i] == spieler for i in range(3)]) or all([spielfeld[i][2 - i] == spieler for i in range(3)]):
        return True

    return False

def spiel_starten():
    spielfeld = [[" " for _ in range(3)] for _ in range(3)]
    aktueller_spieler = "X"
    zuege = 0

    while zuege < 9:
        spielfeld_anzeigen(spielfeld)
        reihe = int(input(f"Spieler {aktueller_spieler}, gib die Reihe ein (0-2): "))
        spalte = int(input(f"Spieler {aktueller_spieler}, gib die Spalte ein (0-2): "))

        if spielfeld[reihe][spalte] == " ":
            spielfeld[reihe][spalte] = aktueller_spieler
            zuege += 1

            if pruefe_gewinner(spielfeld, aktueller_spieler):
                spielfeld_anzeigen(spielfeld)
                print(f"Spieler {aktueller_spieler} gewinnt!")
                return

            aktueller_spieler = "O" if aktueller_spieler == "X" else "X"
        else:
            print("Feld ist bereits besetzt, versuche es erneut.")

    print("Unentschieden!")

spiel_starten()
