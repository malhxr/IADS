def add_contact(address_book, file_name):
    name = input("Enter name: ")
    email = input("Enter email: ")
    # Check for duplicates first
    if any(contact['name'] == name and contact['email'] == email for contact in address_book):
        print(f"\nContact {name} with email {email} already exists.")
    else:
        address_book.append({'name':name,'email':email})
        with open(file_name, 'w') as f:
            for contact in address_book:
                f.write(f"{contact['name']},{contact['email']}\n")
        print("\nContact added successfully")

def search_contact(address_book):
    if len(address_book) == 0:
        print("\nNo contacts.\n")
    else:
        name = input("Enter name to search: ")
        count = 0
        for contact in address_book:
            if name == contact['name']:
                count += 1
                print(f"\nEmail for {name} is {contact['email']}.")
        if count == 0:
            print(f"\nContact not found.")

def list_all_contacts(address_book):
    if len(address_book) == 0:
        print("\nNo Contacts")
    else:
        print("\nAll Contacts")
        for contact in address_book:
            print(f"{contact['name']} - {contact['email']}")

def load_address_book(file_name):
    address_book = []
    try:
        with open(file_name, 'r') as f:
            for line in f:
                name, email = line.strip().split(',')
                address_book.append({'name':name,'email':email})
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

        try:
            user_input = int(input("Enter your choice: "))
            if user_input == 1:
                add_contact(address_book, file_name)
            elif user_input == 2:
                search_contact(address_book)
            elif user_input == 3:
                list_all_contacts(address_book)
            elif user_input == 4:
                print("\nThank you!")
                print("Exiting.")
                break
            else:
                print("\nInvalid input: Enter valid number from 1 to 4.")
        except ValueError:
            print("\nInvalid input: Enter valid number from 1 to 4.")

        


if __name__ == "__main__":
    main()