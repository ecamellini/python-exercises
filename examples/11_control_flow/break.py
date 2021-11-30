"""
Esempio di break in un ciclo while.
"""

contatore = 0
while True:
    print(f"Contatore: {contatore}")
    op = input("Inserisci un'operazione: ")
    if op == 'esci':
        break  # esce dal ciclo, ignorando la condizione
    elif op == '+':
        contatore = contatore + 1
    elif op == '-':
        contatore = contatore - 1

# break mi porta qua!
print('Fine!')
