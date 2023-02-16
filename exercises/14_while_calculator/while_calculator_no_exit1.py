"""
Partendo dall'Esercizio 12, fai in modo che l'utente possa eseguire operazioni
finché non scrive exit, causando così l'uscita dal programma.

>> Senza usare l'istruzione exit()
"""

operation = input("Inserisci un'operazione: ")

continua = True
if operation == "exit":
    continua = False

while continua:

    terms = operation.split()

    x = float(terms[0])
    operator = terms[1]
    y = float(terms[2])

    if operator == "+":
        print(x + y)
    elif operator == "-":
        print(x - y)
    elif operator == "*":
        print(x * y)
    elif operator == "/":
        print(x / y)
    elif operator == "**":
        print(x ** y)
    elif operator == "%":
        print(x % y)
    elif operator == "//":
        print(x // y)
    else:
        print("Operatore non riconosciuto.")

    operation = input("Inserisci un'operazione: ")

    if operation == "exit":
        continua = False
