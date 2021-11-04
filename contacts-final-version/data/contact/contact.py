"""
Define contact data model.
"""


class Contact:
    """
    Contact model class.
    """

    def __init__(self, contact_id, name, surname, phone, email, address, city, country, zipcode):
        self.contact_id = contact_id
        self.name = name
        self.surname = surname
        self.phone = phone
        self.email = email
        self.address = address
        self.city = city
        self.country = country
        self.zipcode = zipcode

    def pretty_print(self):
        """
        Pretty print contact.
        """
        print("\nContact:")
        print(f"\tID: {self.contact_id}")
        print(f"\tName: {self.name}")
        print(f"\tSurname: {self.surname}")
        print(f"\tPhone: {self.phone}")
        print(f"\tEmail: {self.email}")
        print(f"\tAddress: {self.address}")
        print(f"\tCity: {self.city}")
        print(f"\tCountry: {self.country}")
        print(f"\tZipcode: {self.zipcode}\n")
