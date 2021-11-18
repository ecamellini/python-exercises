"""
Boot dell'applicazione. Il file da eseguire per avviarla.
"""

from data.contact.contact_data_json import ContactDataJson
contact_data = ContactDataJson(json_path='contacts.json')

# from data.contact.contact_data_csv import ContactDataCsv
# contact_data = ContactDataCsv(csv_path='contacts.csv')

# from data.contact.contact_data_sqlite import ContactDataSqlite
# contact_data = ContactDataSqlite(db_path='contacts.db')


def create_contact():
    """
    Crea un nuovo contatto.
    """
    print('Creazione di un nuovo contatto:')
    name = input('Inserisci il nome: ')
    surname = input('Inserisci il cognome: ')
    phone = input('Inserisci il numero di telefono: ')
    email = input('Inserisci l\'email: ')
    contact_data.create_contact(
        name,
        surname,
        phone,
        email,
    )


def read_contact():
    """
    Legge un contatto.
    """
    print('Lettura di un contatto:')
    contact_id = input('Inserisci l\'id del contatto: ')
    contact = contact_data.read_contact(contact_id)
    if contact:
        contact.pretty_print()
    else:
        print('Contatto non trovato.')


def update_contact():
    """
    Aggiorna un contatto.
    """
    print('Aggiornamento di un contatto:')
    contact_id = input('Inserisci l\'id del contatto: ')
    contact = contact_data.read_contact(contact_id)
    if contact:
        contact.pretty_print()
        contact.name = input('Inserisci il nome: ')
        contact.surname = input('Inserisci il cognome: ')
        contact.phone = input('Inserisci il numero di telefono: ')
        contact.email = input('Inserisci l\'email: ')
        contact_data.update_contact(contact)
    else:
        print('Contatto non trovato.')


def delete_contact():
    """
    Cancella un contatto.
    """
    print('Cancellazione di un contatto:')
    contact_id = input('Inserisci l\'id del contatto: ')
    contact_data.delete_contact(contact_id)
    print('Contatto cancellato con successo.')


def list_contacts():
    """
    Lista i contatti.
    """
    print('Lista dei contatti:')
    contacts = contact_data.list_contacts()
    if contacts and len(contacts) > 0:
        for contact in contacts:
            contact.pretty_print()
    else:
        print('Nessun contatto trovato.')


def search_contacts():
    print('Cerca tra i contatti:')
    search = input('Inserisci chiave di ricerca: ')
    search_terms = search.split(' ')
    contacts = contact_data.list_contacts()
    for contact in contacts:
        to_search = contact.name + contact.surname + contact.phone + contact.email
        for search_term in search_terms:
            if search_term.lower() in to_search.lower():
                contact.pretty_print()


if __name__ == '__main__':
    # Funzione che riceve comandi dall'utente e li esegue.

    print('Benvenuto in Contacts Manager.')

    print('Operazioni disponibili:')
    print('create: crea un nuovo contatto.')
    print('read: leggi un contatto.')
    print('update: aggiorna un contatto.')
    print('delete: cancella un contatto.')
    print('list: lista i contatti.')
    print('search: cerca tra i contatti.')
    print('exit: esci dal programma.')

    while True:
        operation = input("\nInserire operazione e premere Invio:\n")

        if operation == 'exit':
            exit()
        elif operation == 'create':
            create_contact()
        elif operation == 'read':
            read_contact()
        elif operation == 'update':
            update_contact()
        elif operation == 'delete':
            delete_contact()
        elif operation == 'list':
            list_contacts()
        elif operation == 'search':
            search_contacts()
        else:
            print('Operazione non riconosciuta')
