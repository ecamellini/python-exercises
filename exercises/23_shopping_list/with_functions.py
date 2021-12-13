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

shopping_list = []


def add(item):
    """
    Aggiunge un elemento alla lista.
    """
    shopping_list.append(item)


def show():
    """
    Mostra la lista.
    """
    print(shopping_list)


def remove(item):
    """
    Rimuove un elemento dalla lista.
    """
    if item in shopping_list:
        shopping_list.remove(item)


def clear():
    """
    Cancella la lista.
    """
    shopping_list.clear()


def search(item):
    """
    Cerca un elemento nella lista.
    """
    if item in shopping_list:
        return True
    else:
        return False


print("Benvenuto nella tua lista della spesa!")
print("Inserisci 'add' per aggiungere un elemento alla lista.")
print("Inserisci 'show' per mostrare la lista.")
print("Inserisci 'remove' per rimuovere un elemento dalla lista.")
print("Inserisci 'clear' per cancellare la lista.")
print("Inserisci 'search' per capire se un elemento è nella lista.")
print("Inserisci 'exit' per uscire.")

while True:
    command = input("Inserisci il comando: ")

    if command == "add":
        item = input("Inserisci l'elemento: ")
        add(item)
    elif command == "show":
        show()
    elif command == "remove":
        item = input("Inserisci l'elemento: ")
        remove(item)
    elif command == "clear":
        clear()
    elif command == "search":
        item = input("Inserisci l'elemento: ")
        if search(item):
            print("L'elemento è nella lista.")
        else:
            print("L'elemento non è nella lista.")
    elif command == "exit":
        break
    else:
        print("Comando non riconosciuto.")
