getal1 = int(input("Geef het eerste getal in: "))
getal2 = int(input("Geef het tweede getal in: "))

print("Som", getal1 + getal2)
print("Verschil", getal1 - getal2)
print("Product", getal1 * getal2)
print("Deling", getal1 / getal2)

if getal1 % 2 == 0:
    print("Het getal is even")
else:
    print("Het getal is oneven")

print("Kwadraat", getal1 ** 2)