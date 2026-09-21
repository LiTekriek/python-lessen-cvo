class Werknemer:
    def __init__(self, naam, functie):
        self.naam = naam
        self.functie = functie

    def introductie(self):
        print(f"{self.naam} werkt als een {self.functie}")

collega = Werknemer("Julia", "Barrista")

collega.introductie()