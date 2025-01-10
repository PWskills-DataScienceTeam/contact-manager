# contact_manager.py

# A list to store contacts. Each contact is a dictionary.
contacts = []

# A set to ensure unique phone numbers.
phone_numbers = set()

def add_contact(name, phone, email, address):
    """Adds a new contact to the list."""
    if phone in phone_numbers:
        return "Error: Phone number already exists."
    
    contact = {
        "name": name,
        "phone": phone,
        "email": email,
        "address": address
    }
    contacts.append(contact)
    phone_numbers.add(phone)
    return "Contact added successfully."

def view_contacts(page=1, page_size=5):
    """Displays all contacts with pagination."""
    start = (page - 1) * page_size
    end = start + page_size
    paginated_contacts = contacts[start:end]

    if not paginated_contacts:
        return "No contacts to display."

    result = "\nContacts:\n"
    for idx, contact in enumerate(paginated_contacts, start=start + 1):
        result += f"{idx}. Name: {contact['name']}, Phone: {contact['phone']}, Email: {contact['email']}, Address: {contact['address']}\n"
    return result

def search_contact(query):
    """Searches for a contact by name, phone, or email."""
    results = [
        contact for contact in contacts
        if query.lower() in contact["name"].lower() or
           query in contact["phone"] or
           query.lower() in contact["email"].lower()
    ]
    
    if not results:
        return "No matching contacts found."

    result = "\nSearch Results:\n"
    for contact in results:
        result += f"Name: {contact['name']}, Phone: {contact['phone']}, Email: {contact['email']}, Address: {contact['address']}\n"
    return result

def update_contact(phone, field, new_value):
    """Updates a specific field of a contact identified by phone number."""
    for contact in contacts:
        if contact["phone"] == phone:
            if field in contact:
                contact[field] = new_value
                return "Contact updated successfully."
            else:
                return "Error: Invalid field."
    return "Error: Contact not found."

def delete_contact(phone):
    """Deletes a contact by phone number."""
    global contacts
    for contact in contacts:
        if contact["phone"] == phone:
            contacts.remove(contact)
            phone_numbers.remove(phone)
            return "Contact deleted successfully."
    return "Error: Contact not found."

def export_contacts(file_name="contacts_export.txt"):
    """Exports all contacts to a file."""
    if not contacts:
        return "No contacts to export."

    try:
        with open(file_name, "w") as file:
            file.write("Exported Contacts:\n")
            for contact in contacts:
                file.write(f"Name: {contact['name']}, Phone: {contact['phone']}, Email: {contact['email']}, Address: {contact['address']}\n")
        return f"Contacts exported successfully to {file_name}."
    except Exception as e:
        return f"Error exporting contacts: {e}"
