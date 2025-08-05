from Contacts import *
while True:
    Show_menu()
    choice = input((Fore.LIGHTGREEN_EX) + "Please select (1 - 6) ")
    if choice == "1":
        Add_contact()
    elif choice == "2":
        Search_contact()
    elif choice == "3":
        Edit_contact()
    elif choice == "4":
        Delete_contact()
    elif choice == "5":
        Show_contacts()
    elif choice == "6":
        print((Fore.GREEN) + "Exiting... \n" \
        "Goodluck")
        break
    else:
        print((Fore.RED) + "Invalid choice; Please try again!")
