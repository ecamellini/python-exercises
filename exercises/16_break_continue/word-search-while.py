trovato = False
frase = input("Inserisci una frase: ")

while not trovato:
    parola_da_cercare = input(
        "Inserisci una parola da ricercare nella frase: ")
    for elemento in frase.split():
        print(elemento)
        if parola_da_cercare == elemento:
            trovato = True
            break

    # Qua siamo in fondo al blocco del ciclo
