"""
Riprendi il programma scritto nell'esercizio 14 dove che permette
all'utente di eseguire un'operazione matematica. Modificalo in modo che:
- La logica per eseguire l'operazione sia in una funzione che
    - Prende in input i due valori e l'operatore
    - Restituisce il risultato, oppure None in caso di operatore non riconosciuto
    - Sia documentata con una docstring
"""


def calculate(x, y, operator):
    """
    Applica l'operatore a i parametri x e y e restituisce il risultato.

    Parametri:
    x: un numero
    y: un altro numero
    operator: una stringa che identifica l'operatore (ad esempio: '+')

    Return:
    Restituisce un numero, risultato dell'operazione.
    Restituisce None in caso l'operazione non sia supportata.
    """
    if operator == "+":
        return x + y
    elif operator == "-":
        return x - y
    elif operator == "*":
        return x * y
    elif operator == "/":
        return x / y
    elif operator == "**":
        return x ** y
    elif operator == "%":
        return x % y
    elif operator == "//":
        return x // y
    else:
        return None


while True:
    operation = input("Inserisci un'operazione: ")

    if operation == "exit":
        exit()

    terms = operation.split()

    x = float(terms[0])
    operator = terms[1]
    y = float(terms[2])

    result = calculate(x, y, operator)
    if result:
        print(result)
    else:
        print('Operazione non riconosciuta.')
