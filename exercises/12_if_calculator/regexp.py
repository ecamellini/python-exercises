"""
Soluzione con strumenti che non abbiamo visto a lezione
"""

import re

op = input("Inserisci un'operazione con numeri interi: ")
regexp = r'(\d+) ?([+/*-]) ?(\d+)'
match = re.match(regexp, op)

try:
    op1 = int(match.group(1))
    operand = match.group(2)
    op2 = int(match.group(3))

    if operand == "+":
        print(op1 + op2)
    if operand == "*":
        print(op1 * op2)
    if operand == "/":
        print(op1 / op2)
    if operand == "-":
        print(op1 / op2)
except:
    print("Errore: inserisci un'operazione matematica.")
