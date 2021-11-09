"""
Scrivi un programma che:
- Legge due numeri dall'utente
- Ci dice se il primo numero è maggiore del secondo, stampando True o False
- Ci dice se il primo numero è pari, stampando True o False
"""

x = int(input("Inserisci un numero: "))
y = int(input("Inserisci un altro numero: "))

print("Il primo numero è maggiore del secondo: ", x > y)
print("Il primo numero è pari: ", x % 2 == 0)
