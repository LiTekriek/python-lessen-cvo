klant = input("Naam van de klant: ")
aantal = int(input("Aantal producten: "))

if aantal < 0:
    print("Fout: aantal producten mag niet negatief zijn.")
else:
    prijs = float(input("Prijs per stuk: "))
    btw_percentage = float(input("geef BTW percentage in (6, 12 of 21): "))

subtotaal = aantal * prijs  
btw = subtotaal * (btw_percentage / 100)
totaal = subtotaal + btw

print( "=" * 40)
print("Factuur voor:", klant)
print("Aantal producten:", aantal)
print("Prijs per stuk:", {round(prijs, 2)})
print("- * 40")
print("Subtotaal: $", {round(subtotaal, 2)})
print("BTW (21%): $", {round(btw, 2)})
print("Totaal $", {round(totaal, 2)})
print( "=" * 40)
