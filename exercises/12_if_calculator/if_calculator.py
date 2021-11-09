"""
Scrivi un programma che:
- Permette a un utente di inserire un'operazione, con operatori e operando separati da spazi
- Ad esempio: 2 + 3 o 3 * 4
- La esegue e ne stampa il risultato
"""

operation = input("Inserisci un'operazione: ")

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
