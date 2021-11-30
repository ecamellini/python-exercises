trovato = False
frase = input("Inserisci una frase: ")

while not trovato:
    parola_da_cercare = input(
        "Inserisci una parola da ricercare nella frase: ")
    parole = frase.split()

    for indice in range(len(parole)):
        elemento = parole[indice]
        if parola_da_cercare == elemento:
            print(indice + 1)
            trovato = True
            break

    # Qua siamo in fondo al blocco del ciclo
