lista_della_spesa = []

while True:
    comando = input("Inserisci un comando: ").lower()

    if comando == "add":
        # Aggiungo più elementi separati da virgola
        stringa_input = input(
            "Inserisci un elemento o più elementi separati da virgola: ")
        elementi = stringa_input.split(',')
        for elemento in elementi:
            lista_della_spesa.append(elemento)

    elif comando == "show":
        print(lista_della_spesa)
    elif comando == "exit":
        break
    else:
        print("Comando non riconosciuto.")

    print()
    print()
    print()
