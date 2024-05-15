def add_contact(address_book, file_name):
    name = input("Enter name: ")
    email = input("Enter email: ")
    address_book[name] = email
    with open(file_name, 'w') as f:
        for name,email in address_book.items():
            f.write(f"{name},{email}\n")
    print("Contact added successfully")

def search_contact(address_book):
    name = input("Enter name to search: ")
    if name in address_book:
        print(f"Email for {name} is {address_book[name]}.")
    else:
        print(f"Contact not found.")

def list_all_contacts(address_book):
    if len(address_book) == 0:
        print("\nNo Contacts")
    else:
        print("\nAll Contacts")
        for name,email in address_book.items():
            print(f"{name} - {email}")

def load_address_book(file_name):
    address_book = {}
    try:
        with open(file_name, 'r') as f:
            for line in f:
                name, email = line.strip().split(',')
                address_book[name] = email
    except FileNotFoundError:
        with open(file_name, 'w') as f:
            pass
    return address_book

def main():
    file_name = "address_book.txt"
    address_book = load_address_book(file_name)

    while True:
        print("\nAddress Book Program")
        print("1. Add a new contact")
        print("2. Search for a contact")
        print("3. List all contacts")
        print("4. Quit")

        user_input = int(input("Enter your choice: "))

        if user_input == 1:
            add_contact(address_book, file_name)
        elif user_input == 2:
            search_contact(address_book)
        elif user_input == 3:
            list_all_contacts(address_book)
        elif user_input == 4:
            print("Thank you!")
            print("Exiting.")
            break
        else:
            print("Invalid input.")


if __name__ == "__main__":
    main()