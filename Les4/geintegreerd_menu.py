# geintegreerd_menu.py – gemaakt door Rios Maes

while True:
    print("\n" + "=" * 45)
    print(" HOOFDMENU ERPM-SYSTEEM PRIMABOUW")
    print("=" * 45)
    print("1) BTW-Calculator (Les 3)")
    print("2) Kortingscalculator (Les 4)")
    print("3) Werf- & Stellingveiligheid (Les 4)")
    print("4) Applicatie afsluiten")
    print("=" * 45)

    keuze = input("Maak uw keuze (1-4): ")

    if keuze == "1":
        print("\n--- [OPSTARTEN BTW-CALCULATOR] ---")

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


    elif keuze == "2":
        print("\n--- [OPSTARTEN KORTINGSCALCULATOR] ---")

        print("=" * 45)
        print(" Korting Checker - PrimaBouw BV")
        print("=" * 45)

        totaalbedrag = float(input("Voer het totale orderbedrag in (€): "))

        if totaalbedrag >= 2500:
            korting_pct = 15
        elif totaalbedrag >= 1000:
            korting_pct = 10
        elif totaalbedrag >= 500:
            korting_pct = 5
        else:
            korting_pct = 0

        kortingsbedrag = totaalbedrag * (korting_pct / 100)
        eindbedrag = totaalbedrag - kortingsbedrag

        print("-" * 45)
        print(f"Bruto orderbedrag : €{totaalbedrag:.2f}")
        print(f"Kortingspercentage: {korting_pct}%")
        print(f"Kortingsbedrag : €{kortingsbedrag:.2f}")
        print(f"Netto te betalen : €{eindbedrag:.2f}")
        print("=" * 45)


    elif keuze == "3":
        print("\n--- [OPSTARTEN WERF-VEILIGHEID] ---")
        print("=" * 45)
        print("     Veiligheids-Assistent PrimaBouw BV")
        print("=" * 45)

        wind_kmh = float(input("Wat is de actuele windsnelheid op de werf (km/u)? "))

        if wind_kmh > 60:
            print("❌ CRITIEK GEVAAR: Stoppen met alle werkzaamheden! Evacueer de stellingen.")
        elif wind_kmh > 30:
            netten = input("Zijn de verplichte veiligheidsnetten gemonteerd? (ja/nee): ")
            if netten.lower() == "ja":
                print("⚠️ WAARSCHUWING: Werken toegestaan, maar wees alert op rukwinden.")
            else:
                print("❌ GEVAAR: Werken op hoogte VERBODEN zonder gemonteerde netten!")
        else:
            regen = input("Is er sprake van hevige regen of ijzel? (ja/nee): ")
            if regen.lower() == "ja":
                print("⚠️ WAARSCHUWING: Risico op gladheid. Werken toegestaan met antislip-schoeisel.")
            else:
                print("✅ VEILIG: Normale werkomstandigheden op de stellingen.")

        print("\n--- EXTRA CONTROLE TORENKRAAN ---")

        kraan_hoogte = float(input("Hoe hoog staat de kraanmast (in meters)? "))

        if wind_kmh > 45 and kraan_hoogte > 20:
            print("❌ KRAAN STATUS: Bediening VERBODEN wegens hefboomwind op grote hoogte.")
        elif wind_kmh > 55 or kraan_hoogte > 40:
            print("⚠️ KRAAN STATUS: Alleen bediening door gecertificeerde masters. Wees uiterst voorzichtig.")
        else:
            print("✅ KRAAN STATUS: Werking binnen de normale veiligheidsmarges.")
    elif keuze == "4":
        print("\nBedankt voor het gebruiken van het PrimaBouw systeem. Tot ziens!")
        break
    else:
        print("❌ Ongeldige keuze! Voer een cijfer van 1 tot en met 4 in.")