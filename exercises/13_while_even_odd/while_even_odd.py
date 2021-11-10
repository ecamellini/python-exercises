"""
Scrivi un programma che, dato un numero dall'utente,
stampa "Pari" se è pari, "Dispari" se è dispari.
Il programma poi ripete l'operazione.

Quando la somma dei numeri inseriti supera 100, il programma stampa la somma e termina.
"""

somma = 0  # inizializzo la somma a 0

while somma < 100:
    number = int(input("Inserisci un numero: "))

    somma += number  # aggiungo il numero alla somma

    if number % 2 == 0:
        print("Pari.")
    else:
        print("Dispari.")

print("La somma dei numeri inseriti è:", somma)
print("È > 100, termino il programma.")
