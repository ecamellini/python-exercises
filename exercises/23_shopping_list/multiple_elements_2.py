lista_della_spesa = []

while True:
    comando = input("Inserisci un comando: ").lower()

    if comando == "add":
        # Aggiungo più elementi
        quanti = int(input("Quanti elementi vuoi aggiungere? "))
        for i in range(quanti):
            elemento = input("Inserisci un elemento: ")
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
