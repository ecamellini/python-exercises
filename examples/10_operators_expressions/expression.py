"""
Programma che calcola area e perimetro di un rettangolo
"""

base = float(input("Inserisci la base del rettangolo: "))
altezza = float(input("Inserisci l'altezza del rettangolo: "))

area = base * altezza
print('Area is', area)
# senza le parentesi cambia il risultato
print('Perimeter is', 2 * (base + altezza))
