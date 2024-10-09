class Bankkonto:
    def __init__(self, inhaber, kontostand=0):
        self.inhaber = inhaber
        self.__kontostand = kontostand

    def einzahlen(self, betrag):
        self.__kontostand += betrag
        print(f"{betrag} eingezahlt. Neuer Kontostand ist {self.__kontostand}.")

    def abheben(self, betrag):
        if betrag <= self.__kontostand:
            self.__kontostand -= betrag
            print(f"{betrag} abgehoben. Neuer Kontostand ist {self.__kontostand}.")
        else:
            print("Nicht genügend Guthaben.")

    def kontostand_anzeigen(self):
        print(f"Der Kontostand beträgt: {self.__kontostand}")

if __name__ == "__main__":
    inhaber = input("Name des Kontoinhabers: ")
    konto = Bankkonto(inhaber, float(input("Startkontostand: ")))

    while True:
        print("\nWählen Sie eine Option:")
        print("1. Einzahlen")
        print("2. Abheben")
        print("3. Kontostand anzeigen")
        print("4. Programm beenden")

        wahl = input("Ihre Wahl: ")
        
        if wahl == '1':
            betrag = float(input("Einzahlungsbetrag: "))
            konto.einzahlen(betrag)
        elif wahl == '2':
            betrag = float(input("Abhebungsbetrag: "))
            konto.abheben(betrag)
        elif wahl == '3':
            konto.kontostand_anzeigen()
        elif wahl == '4':
            print("Programm wird beendet.")
            break
        else:
            print("Ungültige Wahl. Bitte erneut versuchen.")

