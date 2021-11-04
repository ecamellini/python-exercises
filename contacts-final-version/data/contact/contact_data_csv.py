"""
Contact data module for contacts stored in a CSV file.
Implements CRUD operations for the contact table.
(CRUD = Create, Read, Update, Delete).
"""

import csv
import os

from data.contact.contact import Contact


class ContactData:
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
        file = open(self.csv_path, mode, encoding="utf-8")
        return file

    def __create_csv(self):
        """
        Crea il CSV file contenente i contatti.
        """
        if os.path.isfile(self.csv_path):
            return

        file = self.__open_csv("w+")
        try:
            writer = csv.writer(file)
            writer.writerow([
                "contact_id",
                "name",
                "surname",
                "phone",
                "email",
                "address",
                "city",
                "country",
                "zipcode"
            ])
        finally:
            file.close()

    def create_contact(self, name, surname, phone, email, address, city, country, zipcode):
        """
        Crea un nuovo contatto nel nostro CSV.
        """

        contacts = self.list_contacts()
        contact_id = 1
        if len(contacts) > 0:
            contact_id = max([int(contact.contact_id)
                             for contact in contacts]) + 1

        file = self.__open_csv("a")
        try:
            writer = csv.writer(file)
            writer.writerow([
                contact_id,
                name,
                surname,
                phone,
                email,
                address,
                city,
                country,
                zipcode
            ])
        finally:
            file.close()

    def read_contact(self, contact_id):
        """
        Restituisce un contatto dal nostro CSV.
        """
        file = self.__open_csv("r")
        try:
            reader = csv.reader(file)
            next(reader)  # Salta la prima riga del CSV
            for row in reader:
                if row[0] == str(contact_id):
                    return Contact(*row)
            else:
                return None

        finally:
            file.close()

    def list_contacts(self):
        """
        Restituisce tutti i contatti dal nostro CSV.
        """
        file = self.__open_csv("r")
        try:
            reader = csv.reader(file)
            next(reader)  # Salta la prima riga del CSV
            return [Contact(*row) for row in reader]
        finally:
            file.close()

    def update_contact(self, contact):
        """
        Aggiorna un contatto nel nostro CSV.
        """
        contact = self.read_contact(contact.contact_id)
        if contact:
            self.delete_contact(contact)
            file = self.__open_csv("w")
            try:
                writer = csv.writer(file)
                writer.writerow([
                    contact.contact_id,
                    contact.name,
                    contact.surname,
                    contact.phone,
                    contact.email,
                    contact.address,
                    contact.city,
                    contact.country,
                    contact.zipcode
                ])
            finally:
                file.close()

    def delete_contact(self, contact_id):
        """
        Cancella un contatto dal nostro CSV.
        """
        file = self.__open_csv("rw")
        try:
            reader = csv.reader(file)
            next(reader)  # Salta la prima riga del CSV
            for row in reader:
                if row[0] != str(contact_id):
                    writer = csv.writer(file)
                    writer.writerow(row)
        finally:
            file.close()
