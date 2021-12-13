"""
Parti dal programma 24
Fai in modo che ogni volta che l'utente modifica la rubrica, il contenuto venga salvato in maniera persistente su un file JSON.
All'avvio, il programma dovrà leggere i contatti dallo stesso file.
"""
import os
import json

contacts = {}
file_path = "contacts.json"
if os.path.isfile(file_path):
    with open(file_path, "r") as f:
        contacts = json.load(f)
else:
    with open(file_path, "w+") as f:
        json.dump(contacts, f)


def create(name, phone, email):
    """
    Crea un nuovo contatto.
    """
    contacts[name] = {"phone": phone, "email": email}
    with open(file_path, "w") as f:
        json.dump(contacts, f)


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
