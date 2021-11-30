trovato = False
frase = input("Inserisci una frase: ")

while not trovato:
    indice = 0
    parola_da_cercare = input(
        "Inserisci una parola da ricercare nella frase: ")
    for elemento in frase.split():
        indice += 1
        # print(f"{indice} ; {elemento}")
        if parola_da_cercare == elemento:
            print(indice)
            trovato = True
            break

    # Qua siamo in fondo al blocco del ciclo
