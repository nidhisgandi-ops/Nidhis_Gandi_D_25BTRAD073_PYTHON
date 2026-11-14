contacts = []


def display_menu():
    print("\n" + "=" * 40)
    print(" CONTACT BOOK MENU ")
    print("=" * 40)
    print("1. Add Contact")
    print("2. Search Contact")
    print("3. Update Contact")
    print("4. Delete Contact")
    print("5. Display All Contacts")
    print("6. Exit")
    print("=" * 40)


def add_contact():
    print("\n--- Add New Contact ---")
    name = input("Enter Name: ").strip()
    phone = input("Enter Phone Number: ").strip()
    email = input("Enter Email Address: ").strip()
    role = input("Enter Role / Scenario (e.g., Personal / Office): ").strip()
    contact_dict = {
        "name": name,
        "phone": phone,
        "email": email,
        "role": role,
    }
    contacts.append(contact_dict)
    print(f" Contact '{name}' added successfully!")


def search_contact():
    print("\n--- Search Contact ---")
    query = input("Enter name to search: ").strip().lower()
    found = []
    for contact in contacts:
        if query in contact["name"].lower():
            found.append(contact)

    if found:
        print(f"\nFound {len(found)} matching contact(s):")
        for i, c in enumerate(found, 1):
            print(
                f"\n[{i}] Name : {c['name']}\n"
                f"    Phone: {c['phone']}\n"
                f"    Email: {c['email']}\n"
                f"    Role : {c['role']}"
            )
    else:
        print(" No matching contact found.")


def update_contact():
    print("\n--- Update Contact ---")
    name_query = input(
        "Enter the exact or partial name of the contact to update: "
    ).strip().lower()
    target_contact = None

    for contact in contacts:
        if contact["name"].lower() == name_query:
            target_contact = contact
            break

    if not target_contact:
        matches = [c for c in contacts if name_query in c["name"].lower()]
        if len(matches) == 1:
            target_contact = matches[0]
        elif len(matches) > 1:
            print("Multiple matches found. Please be more specific.")
            return
        else:
            print(" Contact not found.")
            return

    print(f"\nUpdating contact: {target_contact['name']}")
    new_phone = input(f"Enter new phone [{target_contact['phone']}]: ").strip()
    new_email = input(f"Enter new email [{target_contact['email']}]: ").strip()
    new_role = input(f"Enter new role [{target_contact['role']}]: ").strip()

    if new_phone:
        target_contact["phone"] = new_phone
    if new_email:
        target_contact["email"] = new_email
    if new_role:
        target_contact["role"] = new_role

    print(" Contact updated successfully!")


def delete_contact():
    print("\n--- Delete Contact ---")
    name_query = input("Enter the name of the contact to delete: ").strip().lower()

    global contacts
    initial_length = len(contacts)
    contacts = [c for c in contacts if c["name"].lower() != name_query]

    if len(contacts) < initial_length:
        print(f" Contact '{name_query}' deleted successfully!")
    else:
        print("Contact not found.")


def display_all_contacts():
    print("\n--- All Contacts ---")
    if not contacts:
        print("Your contact book is empty.")
        return

    for i, c in enumerate(contacts, 1):
        print(f"\n--- Contact #{i} ---")
        print(f"Name : {c['name']}")
        print(f"Phone : {c['phone']}")
        print(f"Email : {c['email']}")
        print(f"Role : {c['role']}")


def main():
    contacts.append({
        "name": "Aarav Sharma",
        "phone": "+91 98765 43210",
        "email": "aarav.s@company.com",
        "role": "Project Manager (Organizational)",
    })
    contacts.append({
        "name": "Priya Nair",
        "phone": "+91 91234 56789",
        "email": "priya.nair@gmail.com",
        "role": "Family (Personal)",
    })

    while True:
        display_menu()
        choice = input("Select an option (1-6): ").strip()
        if choice == "1":
            add_contact()
        elif choice == "2":
            search_contact()
        elif choice == "3":
            update_contact()
        elif choice == "4":
            delete_contact()
        elif choice == "5":
            display_all_contacts()
        elif choice == "6":
            print("\nExiting Contact Book. Goodbye!")
            break
        else:
            print(" Invalid choice. Please enter a number between 1 and 6.")


if __name__ == "__main__":
    main()
