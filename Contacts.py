# A mudule for openning menu & doing original actions like add, search, edit, delete and see contacts.
from colorama import *

Contacts = {}
def Show_menu():
    print((Fore.GREEN) + "<<<Contacts Menu>>>")
    print((Fore.RED) + "1. Add contact")
    print((Fore.RED) + "2. Search contact")
    print((Fore.RED) + "3. Edit Number")
    print((Fore.RED) + "4. Delete contact")
    print((Fore.RED) + "5. All contact")
    print((Fore.RED) + "6. Exit")

def Add_contact():
    name = str(input((Fore.CYAN) + "Contact Name: "))
    number = int(input((Fore.BLUE) + "Phone number: "))
    Contacts[name] = number
    print((Fore.GREEN) + "Contact added!")

def Search_contact():
    name = str(input((Fore.CYAN) + "Search name: "))
    if name in Contacts:
        print((Fore.GREEN) + f"{name} -> {Contacts[name]}")
    else:
        print((Fore.RED) + "Contact didn't find!")

def Edit_contact():
    name = str(input((Fore.CYAN) + "Contact name for edit: "))
    if name in Contacts:
        number = int(input((Fore.BLUE) + "New phone number: "))
        Contacts[name] = number
        print((Fore.GREEN) + "The contact updated.")
    else:
        print((Fore.RED) + "Contact didn't find!")

def Delete_contact():
    name = str(input((Fore.CYAN) + "Enter contact's name for delete: "))
    if name in Contacts:
        del Contacts[name]
    else:
        print((Fore.RED) + "Contact not found!")

def Show_contacts():
    if Contacts:
        print((Fore.YELLOW) + "Contacts List: ")
        for name, number in Contacts.items():
            print(f"- {name}: {number}")
    else:
        print((Fore.RED) + "There in no one contact yet!")
