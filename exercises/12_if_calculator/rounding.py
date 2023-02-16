operationString = input("""Inserisci un'operazione.
NOTE:
- massimo due operandi,
- operandi e operatore separati da spazi

Operazione: """)

splitResult = operationString.split()
number1 = float(splitResult[0])
operator = splitResult[1]
number2 = float(splitResult[2])

# result = 0  # giusto per definire la variabile
if operator == "+":
    result = number1 + number2
elif operator == "-":
    result = number1 - number2
elif operator == "*":
    result = number1 * number2
elif operator == "/":
    result = number1 / number2
else:
    print("Operazione non supportata.")
    exit()


print("Il risultato dell'operazione è:")
print(round(result))
