#!/usr/bin/python3

class AddressBook:
    """A class representing an address book.

    Attributes:
        contacts (list): A list to store individual contacts.

    Methods:
        __init__(self):
            Initializes a new instance of the AddressBook class.

        add_contact(self, name, address, phone_number, email):
            Adds a new contact to the address book.

        list_contacts(self):
            Prints the list of contacts in the address book.

    Example:
        address_book = AddressBook()
        address_book.add_contact("John Doe", "123 Main St", "555-1234", "john@example.com")
        address_book.list_contacts()
    """

    def __init__(self):
        """Initializes a new instance of the AddressBook class."""
        self.contacts = []

    def add_contact(self, name, address, phone_number, email):
        """Adds a new contact to the address book.

        Args:
            name (str): The name of the contact.
            address (str): The address of the contact.
            phone_number (str): The phone number of the contact.
            email (str): The email address of the contact.
        """
        contact = {
            'name': name,
            'address': address,
            'phone_number': phone_number,
            'email': email
        }
        self.contacts.append(contact)

    def list_contacts(self):
        """Prints the list of contacts in the address book."""
        print("Contacts in the Address Book:")
        for contact in self.contacts:
            print(f"Name: {contact['name']}")
            print(f"Address: {contact['address']}")
            print(f"Phone Number: {contact['phone_number']}")
            print(f"Email: {contact['email']}")
            print("-" * 30)

if __name__ == "__main__":
    address_book = AddressBook()
    address_book.add_contact("John Doe", "123 Main St", "555-1234", "john@example.com")
    address_book.list_contacts()
