# calculator_menu. py - gemaakt door Rios Maes

while True:
    print("\n" + "=" * 40)
    print("        HoofdMenu")
    print("=" * 40)
    print("1) BTW berekenen")
    print("2) Temperatuur omrekenen")
    print("3) Stoppen")

    keuze = input("Maak een keuze (1-3): ")
    if keuze == "1":
        bedrag = float(input("Geef het bedrag (€): "))
        tarief = int(input("Geef btw-tarief (6, 12 of 21): "))

        btw =  bedrag * (tarief / 100)
        totaal = bedrag + btw

        print("=" * 40)
        print(f"Bedrag exclusief BTW: €{bedrag:.2f}")
        print(f"Btw {tarief}%)    : €{btw:.2f}")
        print(f"Totaal inclusief btw: €{totaal:.2f}")

    elif keuze == "2":
        print("\n1) fahrehnheit naar celsius")
        print("2) celsius naar fahrenheit")

        richting = input("Kies een optie (1-2): ")
        if richting == "1":
            fahrehnheit = float(input("Temperatuur in °F: "))
            celsius = (fahrehnheit - 32) * 5 / 9
            print(f"{fahrehnheit:.1f} °F = {celsius:.1f} °C")

        elif richting == "2":
            celsius = float(input("Temperatuur in °C: "))
            fahrehnheit = (celsius * 9 / 5) + 32
            print(f"{celsius:.1f} °C = {fahrehnheit:.1f} °F")
        
        else:
            print("Ongeldige keuze")
    elif keuze == "3":
        print("Programma wordt afgesloten.")
        break
    
    else:
        print("Ongeldige keuze, probeer opnieuw")
        
