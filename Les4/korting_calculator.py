# korting_calculator.py - gemaakt door Rios Maes

print("=" * 45)
print(" Korting Checker - PrimaBouw BV")
print("=" * 45)

totaalbedrag = float(input("Voer het totale orderbedrag in (€): "))

if totaalbedrag >= 2500:
    korting_percentage = 15
elif totaalbedrag >= 1000:
    korting_percentage = 10
elif totaalbedrag >= 500:
    korting_percentage = 5
else:
    korting_percentage = 0

kortingsbedrag = totaalbedrag * (korting_percentage / 100)
eindbedrag = totaalbedrag - kortingsbedrag

print("=" * 45)
print(f"Bruto orderbedrag: €{totaalbedrag:.2f}")
print(f"Kortingspercentage: {korting_percentage}%")
print(f"Kortingsbedrag: €{kortingsbedrag:.2f}")
print(f"Netto te betalen: €{eindbedrag:.2f}")
print("=" * 45)