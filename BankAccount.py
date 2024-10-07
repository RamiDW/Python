class Bankkonto:
    def __init__(self, inhaber, kontostand=0):
        self.inhaber = inhaber
        self.__kontostand = kontostand  # Kapselung: Privates Attribut

    def einzahlen(self, betrag):
        if betrag > 0:
            self.__kontostand += betrag
            print(f"{betrag} eingezahlt. Neuer Kontostand ist {self.__kontostand}.")
        else:
            print("Einzahlungsbetrag muss positiv sein.")

    def abheben(self, betrag):
        if 0 < betrag <= self.__kontostand:
            self.__kontostand -= betrag
            print(f"{betrag} abgehoben. Neuer Kontostand ist {self.__kontostand}.")
        else:
            print("Ungültiger Abhebungsbetrag.")

    def kontostand_anzeigen(self):
        return self.__kontostand

class Sparkonto(Bankkonto):  # Vererbung
    def __init__(self, inhaber, kontostand=0, zinssatz=0.01):
        super().__init__(inhaber, kontostand)
        self.zinssatz = zinssatz

    def zinsen_hinzufuegen(self):
        zinsen = self._Bankkonto__kontostand * self.zinssatz
        self.einzahlen(zinsen)
        print(f"Zinsen hinzugefügt: {zinsen}. Neuer Kontostand ist {self.kontostand_anzeigen()}.")

# Objekte erstellen
konto1 = Bankkonto("Alice", 1000)
konto2 = Sparkonto("Bob", 2000, 0.05)

# Methoden verwenden
konto1.einzahlen(500)
konto1.abheben(200)
print(f"Alices Kontostand: {konto1.kontostand_anzeigen()}")

konto2.zinsen_hinzufuegen()
konto2.abheben(100)
print(f"Bobs Kontostand: {konto2.kontostand_anzeigen()}")
