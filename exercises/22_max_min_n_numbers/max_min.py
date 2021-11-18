"""
Scrivi un programma che riceve N argomenti da linea di comando.
- Il primo deve essere "max" o "min".
- Di seguito, una serie di numeri.
- Il programma calcola massimo/minimo tra questi numeri, in base al primo arg
"""
import sys


def max_n(*numbers):
    """
    Funzione che trova il valore massimo di un numero di interi
    """

    max_number = int(numbers[0])
    for number in numbers:
        int_number = int(number)
        if int_number > max_number:
            max_number = int_number
    return max_number


def min_n(*numbers):
    """
    Funzione che trova il valore minimo di un numero di interi
    """

    min_number = int(numbers[0])
    for number in numbers:
        int_number = int(number)
        if int_number < min_number:
            min_number = int_number
    return min_number


maxOrMin = sys.argv[1]
if maxOrMin == "max":
    print(max_n(*sys.argv[2:]))
elif maxOrMin == "min":
    print(min_n(*sys.argv[2:]))
