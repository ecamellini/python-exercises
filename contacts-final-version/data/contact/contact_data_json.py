"""
Contact data module for a JSCON file.
Implements CRUD operations for the contacts.
(CRUD = Create, Read, Update, Delete).
"""

import json
import os

from data.contact.contact import Contact


class ContactDataJson:
    """
    Modulo dati per la il JSON file contenente i contatti.
    """

    # Costruttore della classe. Il primo parametro deve essere sempre self
    def __init__(self, json_path):
        self.json_path = json_path
        self.__create_json()

    def __open_json(self, mode):
        """
        Apre il JSON file.
        """
        return open(self.json_path, mode, encoding="utf-8")

    def __create_json(self):
        """
        Crea il JSON file contenente i contatti.
        """
        if os.path.isfile(self.json_path):
            return

        with self.__open_json("w+") as file_write_or_create:
            json.dump([], file_write_or_create)

    def __decode_json_contact(self, json_contact):
        """
        Decodifica un contatto JSON in un oggetto Contact.
        """
        return Contact(
            contact_id=json_contact["contact_id"],
            name=json_contact["name"],
            surname=json_contact["surname"],
            phone=json_contact["phone"],
            email=json_contact["email"],
        )

    def __dump_to_json(self, contacts):
        with self.__open_json("w") as file_write:
            json.dump(contacts, file_write, indent=4)

    def __read_from_json(self):
        with self.__open_json("r") as file_read:
            return json.load(file_read)

    def create_contact(self, name, surname, phone, email):
        """
        Crea un nuovo contatto nel nostro JSON.
        """
        contacts = self.__read_from_json()
        contact_id = 1
        if len(contacts) > 0:
            contact_id = 1 + max([
                int(contact["contact_id"]) for contact in contacts
            ])
        contacts.append(vars(Contact(
            contact_id=contact_id,
            name=name,
            surname=surname,
            phone=phone,
            email=email,
        )))
        self.__dump_to_json(contacts)

    def read_contact(self, contact_id):
        """
        Restituisce un contatto dal nostro JSON.
        """
        contacts = self.__read_from_json()
        for contact in contacts:
            if contact["contact_id"] == int(contact_id):
                return self.__decode_json_contact(contact)

    def list_contacts(self):
        """
        Restituisce tutti i contatti dal nostro JSON.
        """
        contacts = self.__read_from_json()
        return [self.__decode_json_contact(contact) for contact in contacts]

    def update_contact(self, updated_contact):
        """
        Aggiorna un contatto nel nostro JSON.
        """
        contacts = self.__read_from_json()
        for contact in contacts:
            if contact["contact_id"] == int(updated_contact.contact_id):
                contacts.remove(contact)

        contacts.append(vars(updated_contact))
        self.__dump_to_json(contacts)

    def delete_contact(self, contact_id):
        """
        Cancella un contatto dal nostro JSON.
        """
        contacts = self.__read_from_json()
        for contact in contacts:
            if contact["contact_id"] == int(contact_id):
                contacts.remove(contact)
        self.__dump_to_json(contacts)
