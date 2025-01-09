# Simple Contact Book Program

contacts = {}

def add_contact():#function define

    name = input("Enter name: ")
    if name in contacts:
        print("Contact for {name} already exists.")
        return
    phone = input("Enter phone number: ")
    email = input("Enter email : ")
    contacts[name] = {"Phone": phone, "Email": email}
    print("Contact for {name} added.")

def view_contacts(): #another function define

    if not contacts:
        print("No contacts found.")
        return
    print("\nContact List:")
    for name, details in contacts.items(): # for loop
        print("Name: {name}, Phone: {details['Phone']}, Email: {details['Email']}")

def search_contact():
    
    name = input("Enter the name to search: ")
    if name in contacts:
        details = contacts[name]
        print("Name: {name}, Phone: {details['Phone']}, Email: {details['Email']}")
    else:
        print("No contact found for {name}.")

def update_contact(name, new_email):
    
    if name in contacts:
        old_email = contacts[name]
        contacts[name] = new_email
        print(f"Updated {name}'s email from {old_email} to {new_email}.")
    else:
        print(f"{name} is not in the contact list. Add them first.")

def delete_contact():
    
    name = input("Enter the name to delete: ")
    if name in contacts:
        del contacts[name]
        print("Contact for {name} deleted.")
    else:
        print("No contact found for {name}.")

def menu():

    print("\n--- Contact Book Menu ---")
    print("1. Add Contact")
    print("2. View Contacts")
    print("3. Search Contact")
    print("4. update Contact")
    print("5. Delete Contact")
    print("6. Exit")

if __name__ == "__main__":
    while True:
        menu()
        choice = input("Enter your choice (1-6): ")
        if choice == "1":
            add_contact()
        elif choice == "2":
            view_contacts()
        elif choice == "3":
            search_contact()
        elif choice == "4":
            update_contact()
        elif choice == "5":
            delete_contact()
        elif choice == "6":
            print("Exiting Contact Book. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")