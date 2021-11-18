"""
Definisci una funzione che, dati due numeri A e A, stampa:
- A è maggiore, se A è maggiore di B
- A è uguale a B, se A è uguale a B
- B è maggiore, se B è maggiore di A
"""


def print_max(a, b):  # due parametri, a e b
    if a > b:
        print(a, 'è maggiore')
    elif a == b:
        print(a, 'è uguale a', b)
    else:
        print(b, 'è maggiore')


# passiamo direttamente valori letterali come argomenti
print_max(3, 4)

x = 5
y = 7

# passiamo variabili come argomenti: stesso risultato
print_max(x, y)
