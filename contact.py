class Contact:

    contacts = []
    next_id = 1

    def __init__(self, first_name, last_name, email, note):
        """This method should initialize the contact's attributes"""

        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.note = note

        self.id = Contact.next_id
        Contact.next_id += 1

    @classmethod
    def create(cls, first_name, last_name, email, note):
        """This method should call the initializer,
        store the newly created contact, and then return it"""

        contact1 = Contact(first_name, last_name, email, note)
        cls.contacts.append(contact1)

        return contact1

    @classmethod
    def all(cls):
        """This method should return all of the existing contacts"""

        for contact in cls.contacts:
            print(contact.first_name, contact.last_name, contact.email,
                  contact.note)

    @classmethod
    def find(cls, id_number):
        """ This method should accept an id as an argument
        and return the contact who has that id"""

        for contact in cls.contacts:
            if contact.id == id_number:
                return contact
        return False

    def update(self, attribute, value):
        """ This method should allow you to specify
        1. which of the contact's attributes you want to update
        2. the new value for that attribute
        and then make the appropriate change to the contact"""

        if attribute == "first_name":
            self.first_name = value
        elif attribute == "last_name":
            self.last_name = value
        elif attribute == "email":
            self.email = value
        elif attribute == "note":
            self.note = value
        else:
            print("That field does not exist")
            return False

        print("You have updated '{}' to '{}'".format(attribute, value))
        print(self.first_name, self.last_name, self.email, self.note)

    @classmethod
    def find_by(cls, attribute, value):
        """This method should work similarly to the find method above
        but it should allow you to search for a contact using attributes other
        than id by specifying both the name of the attribute and the value
        eg. searching for 'first_name', 'Betty' should return the first contact
        named Betty"""

        for contact in cls.contacts:
            if attribute == "first_name" and contact.first_name == value:
                print(contact.first_name, contact.last_name, contact.email,
                      contact.note)
                return True
            elif attribute == "last_name" and contact.last_name == value:
                print(contact.first_name, contact.last_name, contact.email,
                      contact.note)
                return True
            elif attribute == "email" and contact.email == value:
                print(contact.first_name, contact.last_name, contact.email,
                      contact.note)
                return True
            elif attribute == "note" and contact.note == value:
                print(contact.first_name, contact.last_name, contact.email,
                      contact.note)
                return True

        print("That information does not exist.")
        return False

    @classmethod
    def delete_all(cls):
        """This method should delete all of the contacts"""

        del cls.contacts[:]

    def full_name(self):
        """Returns the full (first and last) name of the contact"""

        print(self.first_name, self.last_name)

    def delete(self):
        """This method should delete the contact
        HINT: Check the Array class docs for built-in methods that might be
        useful here"""

        Contact.contacts.remove(self)


christine = Contact.create("Christine", "Lee", "chris@gmail.com", "new user")
bill = Contact.create("Bill", "Nye", "bill@gmail.com", "second user")
tom = Contact.create("Tom", "Jones", "tom@gmail.com", "third user")
# print(christine.first_name)
# print(bill.note)
# print(Contact.contacts)
# print(len(Contact.contacts))
# print(christine.id)
# print(bill.id)
# Contact.all()
# Contact.find(1)
# Contact.find(3)
# christine.update("note", "new note on file")
# Contact.find_by("email", "chris@gmail.com")
# Contact.find_by("email", "tom1@gmail.com")
# Contact.delete_all()
# print(Contact.contacts)
# christine.full_name()
# bill.full_name()
# tom.full_name()
# print(len(Contact.contacts))
# bill.delete()
# print(len(Contact.contacts))
# print(Contact.contacts[0].first_name)
# print(Contact.contacts[1].first_name)
