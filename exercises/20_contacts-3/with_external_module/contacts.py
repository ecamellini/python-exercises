from contact_store import input_contact, print_contact


print('Operazioni disponibili:')
print('create: salva contatto.')
print('read: leggi contatto.')
print('exit: esci dal programma.')

while True:
    operation = input("\nInserire operazione e premere Invio:\n")

    if operation == 'exit':
        exit()
    elif operation == 'create':
        input_contact()
    elif operation == 'read':
        print_contact()
    else:
        print('Operazione non riconosciuta')
