lista_della_spesa = set([])  # questa lista non conterrà duplicati

# È quello che ci interessa: che un elemento esista o no nella lista
# L'ordine degli elementi non ci interessa

while True:
    comando = input("Inserisci un comando: ").lower()

    if comando == "add":
        elemento = input("Inserisci l'elemento da aggiungere: ")
        # Se aggiungo un duplicato, non verrà aggiunto due volte
        lista_della_spesa.add(elemento)
    elif comando == "show":
        print(lista_della_spesa)
    elif comando == "remove":
        elemento = input("Inserisci l'elemento da cancellare: ")
        if elemento in lista_della_spesa:
            lista_della_spesa.remove(elemento)
        else:
            print("Elemento non trovato.")
    elif comando == "clear":
        lista_della_spesa.clear()
    elif comando == "search":
        elemento = input("Inserisci l'elemento da cercare: ")
        if elemento in lista_della_spesa:
            print("L'elemento è nella lista.")
        else:
            print("L'elemento non è nella lista.")
    elif comando == "exit":
        break
    else:
        print("Comando non riconosciuto.")

    print()
    print()
    print()
