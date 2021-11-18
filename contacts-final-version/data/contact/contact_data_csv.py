"""
Contact data module for contacts stored in a CSV file.
Implements CRUD operations for the contact table.
(CRUD = Create, Read, Update, Delete).
"""

import csv
import os

from data.contact.contact import Contact


HEADER = ["contact_id", "name", "surname", "phone", "email"]


class ContactDataCsv:
    """
    Modulo dati per la il CSV file contenente i contatti.
    """

    # Costruttore della classe. Il primo parametro deve essere sempre self
    def __init__(self, csv_path):
        self.csv_path = csv_path
        self.__create_csv()

    def __open_csv(self, mode):
        """
        Apre il CSV file.
        """
        return open(self.csv_path, mode, encoding="utf-8")

    def __create_csv(self):
        """
        Crea il CSV file contenente i contatti.
        """
        if os.path.isfile(self.csv_path):
            return

        with self.__open_csv("w+") as file_create_and_write:
            writer = csv.writer(file_create_and_write)
            writer.writerow(HEADER)

    def __write_contact_row(self, csv_writer, contact):
        csv_writer.writerow([
            contact.contact_id,
            contact.name,
            contact.surname,
            contact.phone,
            contact.email
        ])

    def create_contact(self, name, surname, phone, email):
        """
        Crea un nuovo contatto nel nostro CSV.
        """

        contacts = self.list_contacts()
        contact_id = 1
        if contacts and len(contacts) > 0:
            contact_id = 1 + max([
                int(contact.contact_id) for contact in contacts
            ])

        with self.__open_csv("a") as file_append:
            writer = csv.writer(file_append)
            self.__write_contact_row(
                writer,
                Contact(contact_id, name, surname, phone, email)
            )

    def read_contact(self, contact_id):
        """
        Restituisce un contatto dal nostro CSV.
        """
        with self.__open_csv("r") as file_read:
            reader = csv.reader(file_read)
            for row in reader:
                if row[0] == str(contact_id):
                    return Contact(*row)

            return None

    def list_contacts(self):
        """
        Restituisce tutti i contatti dal nostro CSV.
        """
        with self.__open_csv("r") as file_read:
            reader = csv.reader(file_read)
            try:
                next(reader)  # Salta la prima riga del CSV
            except StopIteration:
                return None
            return [Contact(*row) for row in reader]

    def update_contact(self, updated_contact):
        """
        Aggiorna un contatto nel nostro CSV.
        """
        contacts = self.list_contacts()
        if contacts:
            with self.__open_csv("w") as file_write:
                writer = csv.writer(file_write)
                writer.writerow(HEADER)
                for contact in contacts:
                    if contact.contact_id == updated_contact.contact_id:
                        self.__write_contact_row(writer, updated_contact)
                    else:
                        self.__write_contact_row(writer, contact)

    def delete_contact(self, contact_id):
        """
        Cancella un contatto dal nostro CSV.
        """
        contacts = self.list_contacts()
        if contacts:
            with self.__open_csv("w") as file_write:
                writer = csv.writer(file_write)
                writer.writerow(HEADER)
                for contact in contacts:
                    if contact.contact_id != contact_id:
                        self.__write_contact_row(writer, contact)
