"""
Contact data module for a SQLite database.
Implements CRUD operations for the contact table.
(CRUD = Create, Read, Update, Delete).
"""

import sqlite3

from data.contact.contact import Contact


class ContactDataSqlite:
    """
    Modulo dati per la tabella Contact del nostro database.
    """

    # Costruttore della classe. Il primo parametro deve essere sempre self
    def __init__(self, db_path):
        self.db_path = db_path
        self.__create_table()

    def __create_table(self):
        """
        Crea la tabella Contact nel nostro database.
        """
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()

        # Creiamo la tabella per gli studenti, se non esiste già
        try:
            cursor.execute("""CREATE TABLE Contact(
            contact_id integer primary key,
            name text,
            surname text,
            phone text unique,
            email text unique
        )""")
        except sqlite3.OperationalError:
            pass

        conn.commit()
        conn.close()

    def create_contact(self, name, surname, phone, email):
        """
        Crea un nuovo contatto nel nostro database.
        """
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()

        # Creiamo un nuovo contatto
        try:
            cursor.execute("""
            INSERT INTO Contact(contact_id, name, surname, phone, email)
            VALUES(?, ?, ?, ?, ?)""", (
                None,
                name,
                surname,
                phone,
                email
            ))
        except sqlite3.IntegrityError as error:
            print("Errore nella creazione del contatto:")
            print(error)

        conn.commit()
        conn.close()

    def read_contact(self, contact_id):
        """
        Restituisce un contatto dal nostro database.
        """
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()

        # Restituiamo un contatto
        cursor.execute(
            """SELECT * FROM Contact WHERE contact_id = ?""", (contact_id,))
        result = cursor.fetchone()

        conn.close()
        if result:
            return Contact(*result)
        else:
            return None

    def list_contacts(self):
        """
        Restituisce tutti i contatti dal nostro database.
        """
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()

        # Restituiamo tutti i contatti
        cursor.execute("SELECT * FROM Contact")
        result = cursor.fetchall()

        conn.close()
        if result:
            return [Contact(*row) for row in result]
        else:
            return None

    def update_contact(self, contact):
        """
        Aggiorna un contatto nel nostro database.
        """
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()

        # Aggiorniamo un contatto
        try:
            cursor.execute("""
            UPDATE Contact SET name = ?, surname = ?, phone = ?, email = ?
            WHERE contact_id = ?""", (
                contact.name,
                contact.surname,
                contact.phone,
                contact.email,
                contact.contact_id
            ))
        except sqlite3.IntegrityError as error:
            print("Errore nell'aggiornamento del contatto:")
            print(error)

        conn.commit()
        conn.close()

    def delete_contact(self, contact_id):
        """
        Cancella un contatto dal nostro database.
        """
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()

        # Cancelliamo un contatto

        cursor.execute(
            """DELETE FROM Contact WHERE contact_id = ?""", (contact_id,)
        )

        conn.commit()
        conn.close()
