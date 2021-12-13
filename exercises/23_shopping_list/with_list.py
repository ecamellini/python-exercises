"""
Scrivi un programma che gestisca una lista della spesa.
Il programma deve supportare i seguenti comandi:
- add: chiede all'utente un elemento da aggiungere alla lista, e lo aggiunge
- show: mostra la lista
- remove: chiede all'utente un elemento da rimuovere dalla lista, e lo rimuove
- clear: rimuove tutti gli elementi dalla lista
- search: chiede all'utente un elemento da cercare nella lista, e dice se c'è o no
- exit: esce dal programma
"""

lista_della_spesa = []

while True:
    comando = input("Inserisci un comando: ").lower()

    if comando == "add":
        elemento = input("Inserisci l'elemento da aggiungere: ")
        lista_della_spesa.append(elemento)
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
