"""
Boot dell'applicazione. Il file da eseguire per avviarla.
"""

from data.contact.contact_data_csv import ContactData


contact_data = ContactData(csv_path='contacts.csv')


def create_contact():
    """
    Crea un nuovo contatto.
    """
    print('Creazione di un nuovo contatto')
    name = input('Inserisci il nome: ')
    surname = input('Inserisci il cognome: ')
    phone_number = input('Inserisci il numero di telefono: ')
    email = input('Inserisci l\'email: ')
    address = input('Inserisci l\'indirizzo: ')
    city = input('Inserisci la città: ')
    province = input('Inserisci la provincia: ')
    zip_code = input('Inserisci il codice postale: ')
    contact_data.create_contact(
        name,
        surname,
        phone_number,
        email,
        address,
        city,
        province,
        zip_code
    )


def read_contact():
    """
    Legge un contatto.
    """
    print('Lettura di un contatto')
    contact_id = input('Inserisci l\'id del contatto: ')
    contact = contact_data.read_contact(contact_id)
    if contact:
        contact.pretty_print()
    else:
        print('Contatto non trovato')


def update_contact():
    """
    Aggiorna un contatto.
    """
    print('Aggiornamento di un contatto')
    contact_id = input('Inserisci l\'id del contatto: ')
    contact = contact_data.read_contact(contact_id)
    if contact:
        contact.pretty_print()
        contact.name = input('Inserisci il nome: ')
        contact.surname = input('Inserisci il cognome: ')
        contact.phone_number = input('Inserisci il numero di telefono: ')
        contact.email = input('Inserisci l\'email: ')
        contact.address = input('Inserisci l\'indirizzo: ')
        contact.city = input('Inserisci la città: ')
        contact.province = input('Inserisci la provincia: ')
        contact.zip_code = input('Inserisci il codice postale: ')
        contact_data.update_contact(contact)
    else:
        print('Contatto non trovato')


def delete_contact():
    """
    Cancella un contatto.
    """
    print('Cancellazione di un contatto')
    contact_id = input('Inserisci l\'id del contatto: ')
    contact_data.delete_contact(contact_id)
    print('Contatto cancellato con successo')


def list_contacts():
    """
    Lista i contatti.
    """
    print('Lista dei contatti')
    contacts = contact_data.list_contacts()
    for contact in contacts:
        contact.pretty_print()


if __name__ == '__main__':
    # Funzione che riceve comandi dall'utente e li esegue.

    print('Benvenuto in Contacts Manager')

    print('Operazioni disponibili:')
    print('create: crea un nuovo contatto')
    print('read: leggi un contatto')
    print('update: aggiorna un contatto')
    print('delete: cancella un contatto')
    print('list: lista i contatti')
    print('exit: esci dal programma')

    while True:
        operation = input("\nInserire operazione\n")

        if(operation == 'exit'):
            exit()
        elif (operation == 'create'):
            create_contact()
        elif (operation == 'read'):
            read_contact()
        elif (operation == 'update'):
            update_contact()
        elif (operation == 'delete'):
            delete_contact()
        elif (operation == 'list'):
            list_contacts()
        else:
            print('Operazione non riconosciuta')
