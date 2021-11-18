"""
Scrivi una funzione che, dati N numeri, trova il valore massimo.
Non usare la funzione predefinita di Python max.
"""


def max_n(*numbers):
    """
    Funzione che trova il valore massimo di un numero di interi
    """

    max_number = numbers[0]
    for number in numbers:
        if number > max_number:
            max_number = number
    return max_number


print(max_n(1, 2, 3, 10, 5, 28, 7, 99, 9, 10))
