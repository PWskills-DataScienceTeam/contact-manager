from contact_manager import (
    add_contact,
    view_contacts,
    search_contact,
    update_contact,
    delete_contact,
    export_contacts,
)

def main():
    while True:
        print("\nContact Manager")
        print("1. Add New Contact")
        print("2. View All Contacts")
        print("3. Search for a Contact")
        print("4. Update Contact Information")
        print("5. Delete a Contact")
        print("6. Export Contacts")
        print("7. Exit")
        
        choice = input("Enter your choice (1-7): ").strip()
        
        if choice == "1":
            name = input("Enter name: ").strip()
            phone = input("Enter phone: ").strip()
            email = input("Enter email: ").strip()
            address = input("Enter address: ").strip()
            print(add_contact(name, phone, email, address))
        
        elif choice == "2":
            page = int(input("Enter page number (default 1): ") or 1)
            print(view_contacts(page))
        
        elif choice == "3":
            query = input("Enter name, phone, or email to search: ").strip()
            print(search_contact(query))
        
        elif choice == "4":
            phone = input("Enter phone number of the contact to update: ").strip()
            field = input("Enter the field to update (name, phone, email, address): ").strip()
            new_value = input(f"Enter the new value for {field}: ").strip()
            print(update_contact(phone, field, new_value))
        
        elif choice == "5":
            phone = input("Enter phone number of the contact to delete: ").strip()
            print(delete_contact(phone))
        
        elif choice == "6":
            print(export_contacts())
        
        elif choice == "7":
            print("Exiting Contact Manager. Goodbye!")
            break
        
        else:
            print("Invalid choice! Please try again.")

if __name__ == "__main__":
    main()
