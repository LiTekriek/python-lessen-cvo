# syntax_oef.py - SyntaxError oefeningen

naam = input("Wat is je naam? ")
print("Hallo " + naam)

getal = int(input("Geef een getal: "))
if getal > 10:
    print("Groot getal!")

temperatuur = float(input("Temperatuur in °C: "))
if temperatuur > 37.5:
    print("Koorts!")

print("Het bedrag is: " + str(100 * 1.21))

print(f"Ik ben {leeftijd} jaar oud.")