"""
Riprendiamo il programma per salvare un contatto (esercizio 17).
Riscrivilo usando due funzioni per salvare
e stampare il contatto, con argomenti passati per nome.
"""

contact_name = ""
contact_surname = ""
contact_phone = ""
contact_email = ""


def create(name, surname, phone, email):
    """
    Salva il contatto.
    """
    global contact_name, contact_surname, contact_phone, contact_email
    contact_name = name
    contact_surname = surname
    contact_phone = phone
    contact_email = email


def read():
    """
    Stampa il contatto.
    """
    print("\nContatto:")
    print("Nome: " + contact_name)
    print("Cognome: " + contact_surname)
    print("Telefono: " + contact_phone)
    print("Email: " + contact_email)


print('Operazioni disponibili:')
print('create: salva contatto.')
print('read: leggi contatto.')
print('exit: esci dal programma.')

while True:
    operation = input("\nInserire operazione e premere Invio:\n")

    if operation == 'exit':
        exit()
    elif operation == 'create':
        print("Inserisci il tuo contatto:")
        create(
            name=input("Nome: "),
            surname=input("Cognome: "),
            phone=input("Telefono: "),
            email=input("Email: ")
        )
    elif operation == 'read':
        read()
    else:
        print('Operazione non riconosciuta')
