# werf_veiligheid.py – gemaakt door Kris Dierickx
print("=" * 45)
print("     Veiligheids-Assistent PrimaBouw BV")
print("=" * 45)
wind_kmh = float(input("Wat is de actuele windsnelheid op de werf (km/u)? "))
if wind_kmh > 60:
    print("❌ CRITIEK GEVAAR: Stoppen met alle werkzaamheden! Evacueer de stellingen.")
elif wind_kmh > 30:
    # Genest niveau 1: De wind is matig tot krachtig. Status hangt af van veiligheidsnetten.
    netten = input("Zijn de verplichte veiligheidsnetten gemonteerd? (ja/nee): ")  
    if netten.lower() == "ja":
        print("⚠️ WAARSCHUWING: Werken toegestaan, maar wees alert op rukwinden.")
    else:
        print("❌ GEVAAR: Werken op hoogte VERBODEN zonder gemonteerde netten!")
else:
    # Genest niveau 2: Veilige wind, maar hoe zit het met neerslag?
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
    print("⚠️ KRAAN STATUS: Alleen bediening door gecertificeerde medewerkers.")

else:
    print("✅ KRAAN STATUS: Werking binnen de normale veiligheidsmarges.")