# Memory of our program
firstName = None
lastName = None
phone = None
eMail = None

command = None
# -------------


while True:
    command = input("""
Inserisci un comando:
(comandi supportati: create, read, delete, exit)
""").lower().strip()

    if command == "create":
        firstName = input("Inserisci il nome: ")
        lastName = input("Inserisci il cognome: ")
        phone = input("Inserisci il telefono: ")
        eMail = input("Inserisci il e-mail: ")
    elif command == "read":
        if firstName is None:
            print("Nessun contatto in memoria.")
        else:
            print(firstName)
            print(lastName)
            print(phone)
            print(eMail)
    elif command == "delete":
        firstName = None
        lastName = None
        phone = None
        eMail = None
    elif command == "exit":
        # oppure exit() -- dopo il ciclo comunque non c'è nulla
        break
    else:
        print("Comando non riconosciuto.")
