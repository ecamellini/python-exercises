"""
Esempi di visibilità delle variabili rispetto a una funzione.
"""


def func(x):
    print('x locale è', x)
    x = 2
    print('Ho modificato la x locale a', x)


# x non esiste qua, siamo fuori dalla funzione!
# print(x) darebbe errore

func(4)

x = 50  # x definita nel blocco di codice principale
print('x esterna è', x)
func(x)  # la x dentro alla funzione è diversa, x esterna non verrà modificata
print('x esterna è ancora', x)
