"""
Definisci una funzione che, dati due numeri A e A, restituisce il massimo.
"""


def maximum(x, y):
    """
    Dati due valori, restituisce il massimo.

    x: il primo dei due valori.
    y: il secondo dei due valori.
    """
    if x > y:
        return x
    else:
        return y


# The same string is visualized when using help(maximum)
print(maximum.__doc__)
