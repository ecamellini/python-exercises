"""
Esempio di break e continue in un ciclo while.
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
    elif op == '=':
        continue
    else:
        print("Operazione non riconosciuta.")
        continue  # non fa niente e salta al giro successivo

# break mi porta qua!
print('Fine!')
