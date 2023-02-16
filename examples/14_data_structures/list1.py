"""
Programma per l'inventario di una biblioteca.
Per ogni libro, salviamo solo il titolo.
Il codice del libro è il suo indice nel catalogo.
Cioè: il primo libro ha codice 0, il non libro ha codice 8.

Deve permettere all'utente di:
1. Visualizzare una lista dei libri presenti
2. Inserire un nuovo libro
3. Dato il codice di un libro, stampane il titolo
4. Dato il codice di un libro, aggiornane il titolo
"""

booksCatalogue = [
    'Il Signore degli Anelli',
    'Harry Potter e la Pietra Filosofale',
    "Lo Zen e L'Arte della Manutenzione della Motocicletta"
]

print("Il primo libro nel catalogo è: ")
print(booksCatalogue[0])

while True:
    command = input(
        "\nInserisci un comando (add, list, exit, searchByCode, updateTitle):")

    if command == "add":
        bookTitle = input(
            "Inserisci il titolo del libro da aggiungere al catalogo: "
        )
        booksCatalogue.append(bookTitle)
    elif command == "list":
        for book in booksCatalogue:
            print(book)
    elif command == "searchByCode":
        bookCode = int(input("Inserisci il codice del libro: "))
        print(booksCatalogue[bookCode])
    elif command == "updateTitle":

        bookCode = int(input("Inserisci il codice del libro: "))
        newTitle = input("Inserisci il nuovo titolo del libro: ")
        booksCatalogue[bookCode] = newTitle

    elif command == "exit":
        break
    else:
        print("Comando non supportato.")
