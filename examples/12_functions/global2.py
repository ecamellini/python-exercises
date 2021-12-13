"""
Esempio di variabile globale.
"""


x = 50


def func():
    global x

    print('x è', x)
    x = 2
    print('Cambio il valore globale di x a', x)


func()
print('Il valore di x è', x)  # stampa 2
