"""
Scrivi un programma che gestisca una rubrica telefonica.
Il programma deve supportare le seguenti funzioni:
- create: crea un nuovo contatto, chiedendo all'utente nome, telefono e email.
- read: stampa il contatto, chiedendo all'utente il nome.
- read_all: stampa tutti i contatti.
- search: cerca un contatto, chiedendo all'utente il termine da cercare.
- exit: termina il programma.
"""

contacts = {}


def create(name, phone, email):
    """
    Crea un nuovo contatto.
    """
    contacts[name] = {"phone": phone, "email": email}


def read(name):
    """
    Stampa il contatto.
    """
    if name in contacts:
        print(f"\nContatto: {name}")
        print(f"Telefono: {contacts[name]['phone']}")
        print(f"Email: {contacts[name]['email']}")
    else:
        print("\nContatto non trovato.")


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
    for name, details in contacts.items():
        if (search_term in name or search_term in details["phone"] or search_term in details["email"]):
            read(name)


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
        name = input("Inserisci il nome del contatto: ")
        phone = input("Inserisci il numero di telefono del contatto: ")
        email = input("Inserisci l'email del contatto: ")
        create(name, phone, email)
    elif command == "read":
        name = input("Inserisci il nome del contatto: ")
        read(name)
    elif command == "read_all":
        read_all()
    elif command == "search":
        search_term = input("Inserisci il termine da cercare: ")
        search(search_term)
    elif command == "exit":
        break
    else:
        print("Comando non riconosciuto.")
