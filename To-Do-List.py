def menue_anzeigen():
    print("1. Aufgabe hinzufügen")
    print("2. Aufgaben anzeigen")
    print("3. Aufgabe entfernen")
    print("4. Beenden")

def aufgabe_hinzufuegen(aufgaben):
    aufgabe = input("Aufgabe eingeben: ")
    aufgaben.append(aufgabe)
    print("Aufgabe hinzugefügt.")

def aufgaben_anzeigen(aufgaben):
    if aufgaben:
        print("#################")
        for i, aufgabe in enumerate(aufgaben, 1):
            print(f"{i}. {aufgabe}")
        print("#################\n")  # Zeilenumbruch hinzugefügt
    else:
        print("Keine Aufgaben gefunden.")

def aufgabe_entfernen(aufgaben):
    aufgaben_anzeigen(aufgaben)
    aufgaben_num = int(input("Nummer der zu entfernenden Aufgabe eingeben: "))
    if 0 < aufgaben_num <= len(aufgaben):
        entfernte_aufgabe = aufgaben.pop(aufgaben_num - 1)
        print(f"Aufgabe entfernt: {entfernte_aufgabe}")
    else:
        print("Ungültige Aufgabennummer.")

def hauptprogramm():
    aufgaben = []
    while True:
        menue_anzeigen()
        wahl = input("Wahl eingeben: ")
        if wahl == "1":
            aufgabe_hinzufuegen(aufgaben)
        elif wahl == "2":
            aufgaben_anzeigen(aufgaben)
        elif wahl == "3":
            aufgabe_entfernen(aufgaben)
        elif wahl == "4":
            break
        else:
            print("Ungültige Wahl. Bitte erneut versuchen.")

if __name__ == "__main__":
    hauptprogramm()
