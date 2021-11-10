"""
Scrivi un programma che:

Permette all'utente di eseguire vari comandi all'infinito, finché non scrive il comando `exit`.
I comandi supportati sono:
- `create` — chiede all'utente nome, cognome, telefono, e email di un contatto, e li salva
- `read` — stampa i dati del contatto salvato
- `exit` — esce dal programma
"""

name = ""
surname = ""
phone = ""
email = ""

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
        name = input("Nome: ")
        surname = input("Cognome: ")
        phone = input("Telefono: ")
        email = input("Email: ")
        print("\nContatto salvato!")
    elif operation == 'read':
        print("\nContatto:")
        print("Nome: " + name)
        print("Cognome: " + surname)
        print("Telefono: " + phone)
        print("Email: " + email)
    else:
        print('Operazione non riconosciuta')
