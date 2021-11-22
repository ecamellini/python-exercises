"""
Scrivi un programma che:
- Legge tre stringhe dall'utente
- Le stampa sulla stessa riga, separate da una virgola e con un punto alla fine

Esempio:
se l'utente inserisce A  B  C
Il programma stampa A, B, C.
"""

A = input("Inserisci la prima stringa: ")
B = input("Inserisci la seconda stringa: ")
C = input("Inserisci la terza stringa: ")

# Soluzione A
print(A + ", " + B + ", " + C + ".")

# Soluzione B
print(f'{A},{B},{C}.')
