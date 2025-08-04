# A mudule for openning menu & doing original actions like add, search, edit, delete and see contacts.

Contacts = {}
def Show_menu():
    print("<<<Contacts Menu>>>")
    print("1. Add contact")
    print("2. Search contact")
    print("3. Edit Number")
    print("4. Delete contact")
    print("5. All contact")
    print("6. Exit")

def Add_contact():
    name = str(input("Contact Name: "))
    number = int(input("Phone number: "))
    Contacts[name] = number
    print("Contact added!")

def Search_contact():
    name = str(input("Search name: "))
    if name in Contacts:
        print(f"{name} -> {Contacts[name]}")
    else:
        print("Contact didn't find!")

def Edit_contact():
    name = str(input("Contact name for edit: "))
    if name in Contacts:
        number = int(input("New phone number: "))
        Contacts[name] = number
        print("The contact updated.")
    else:
        print("Contact didn't find!")

def Delete_contact():
    name = str(input("Enter contact's name for delete: "))
    if name in Contacts:
        del Contacts[name]
    else:
        print("Contact not found!")

def Show_contacts():
    if Contacts:
        print("Contacts List: ")
        for name, number in Contacts.items():
            print(f"- {name}: {number}")
    else:
        print("There in no one contact yet!")
