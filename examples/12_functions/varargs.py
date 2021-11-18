"""
Esempio di funzione che riceve un numero arbitrario/variabile di argomenti (VarArgs)
"""


def print_numbers(label, *numbers):
    print(label)

    # itera sugli oggetti in numbers
    for number in numbers:
        print(number)


print_numbers("Numeri:", 1, 2, 3, 4)
