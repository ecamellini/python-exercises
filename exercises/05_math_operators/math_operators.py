"""
Scrivi un programma che:
- Legge due numeri interi inseriti dall'utente
- Stampa il risultato di somma, sottrazione, moltiplicazione, potenza, divisione, resto
"""

x = input("Inserisci un numero intero: ")
y = input("Inserisci un altro numero intero: ")

x = int(x)
y = int(y)

print("Somma:", x + y)
print("Sottrazione:", x - y)
print("Moltiplicazione:", x * y)
print("Potenza:", x ** y)
print("Divisione:", x / y)
print("Resto:", x % y)
