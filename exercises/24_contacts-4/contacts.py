"""
Scrivi un programma che gestisca una rubrica telefonica.
Il programma deve supportare le seguenti funzioni:
- create: crea un nuovo contatto, chiedendo all'utente id, nome, cognome, telefono e email.
- read: stampa il contatto, chiedendo all'utente l'id.
- read_all: stampa tutti i contatti.
- search: cerca un contatto, chiedendo all'utente il termine da cercare.
- exit: termina il programma.
"""

contacts = {}


def create(id, name, surname, phone, email):
    """
    Crea un nuovo contatto.
    """
    contacts[id] = {"name": name, "surname": surname,
                    "phone": phone, "email": email}


def read(id):
    """
    Stampa il contatto.
    """
    print("\nContatto:")
    print("Nome: " + contacts[id]["name"])
    print("Cognome: " + contacts[id]["surname"])
    print("Telefono: " + contacts[id]["phone"])
    print("Email: " + contacts[id]["email"])


def read_all():
    """
    Stampa tutti i contatti.
    """
    print("\nContatti:")
    for contact in contacts:
        read(contact)


def search(search_term):
    """
    Cerca un contatto.
    """
    print("\nContatti:")
    for contact in contacts:
        if (search_term in contacts[contact]["name"] or
            search_term in contacts[contact]["surname"] or
            search_term in contacts[contact]["phone"] or
                search_term in contacts[contact]["email"]):
            read(contact)


print("\nBenvenuto nel programma di gestione dei contatti.")
print("\nI comandi disponibili sono:")
print("\t- create: crea un nuovo contatto")
print("\t- read: stampa un contatto")
print("\t- read_all: stampa tutti i contatti")
print("\t- search: cerca un contatto")
print("\t- exit: esci dal programma")

while True:
    command = input("\nInserisci il comando: ")
    if command == "create":
        id = input("Inserisci l'id del contatto: ")
        name = input("Inserisci il nome del contatto: ")
        surname = input("Inserisci il cognome del contatto: ")
        phone = input("Inserisci il numero di telefono del contatto: ")
        email = input("Inserisci l'email del contatto: ")
        create(id, name, surname, phone, email)
    elif command == "read":
        id = input("Inserisci l'id del contatto: ")
        read(id)
    elif command == "read_all":
        read_all()
    elif command == "search":
        search_term = input("Inserisci il termine da cercare: ")
        search(search_term)
    elif command == "exit":
        break
    else:
        print("Comando non riconosciuto.")
