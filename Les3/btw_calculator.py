# btw-calculator.py - gemaakt door Rios Maes

print("=" * 45)
print(" BTW-Calculator - PrimaBouw BV")
print("=" * 45)
gebruiker = input("Jouw naam: ")
print("Welkom, " + gebruiker + "!")

bedrag_str = input("Voer het bedrag in (excl. BTW in €):")
bedrag = float(bedrag_str)
tarief_str = input("Welk BTW-tarief? (6, 12 of 21): ")
tarief = int(tarief_str)

btw_bedrag = bedrag * (tarief / 100)
totaal = bedrag + btw_bedrag

btw_pct_van_totaal = (btw_bedrag / totaal) * 100


print("-" * 45)
print(f"Bedrag excl. BTW : €{bedrag:.2f}")
print(f"BTW ({tarief}%)        : €{btw_bedrag:.2f}")
print(f"Totaal incl. BTW : €{totaal:.2f}")
print(f"BTW als % van totaal : {btw_pct_van_totaal:.1f}%")
print("=" * 45)

nog_een = input("\nWil je nog een berekening? (ja/nee°: ")
if nog_een.lower() == "ja":
    print("Start het script opnieuw om een nieuwe berekening te doen.")
else:
    print("Tot de volgende keer, " + gebruiker + "!")