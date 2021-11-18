"""
Funzione per stampare Hello World!
"""


def say_hello():
    # blocco appartenente alla funzione
    print('Hello World!')
# Fine della funzione


def say_hello_to(name, surname):
    print(f'Hello {name} {surname}!')


say_hello()  # chiama la funzione
say_hello()  # chiamala di nuovo
say_hello_to('Mario', 'Rossi')  # chiama la funzione con parametri
say_hello_to('Paolo', 'Rossi')  # chiamala di nuovo
