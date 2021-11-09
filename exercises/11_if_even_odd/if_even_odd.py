"""
Scrivi un programma che, dato un numero dall'utente:
- Stampa "Pari" se è pari
- Stampa "Dispari" se è dispari
- Il numero deve essere positivo, altrimenti il programma termina
"""

number = int(input("Inserisci un numero: "))

if number < 0:
    print("Il numero deve essere positivo.")
    exit()

if number % 2 == 0:
    print("Pari.")
else:
    print("Dispari.")
