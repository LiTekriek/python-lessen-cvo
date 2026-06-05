# temp_calculator.py - gemaakt door Rios Maes
# C = (F - 32) * 5 / 9

print("=" * 40)
print("  Temperatuuromrekening F → C")
print("=" * 40)

fahrenheit = float(input("Geef een temperatuur in Fahrenheit: "))

celsius = (fahrenheit - 32) * 5 / 9
print(f"{fahrenheit:.1f} °F = {celsius:.1f} °C")

# F = (C * 9 / 5) + 32

celsius_input = float(inpiut("\nGeef een temperatuur in Celsius: "))
fahrenheit_resultaat = (celsius_input * 9 / 5) + 32
print(f"{celsius_input:.1f} °C = {fahrenheit_resultaat:.1f} °F")