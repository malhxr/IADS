def add_contact(address_book, file_name):
    '''
    This function takes name and email from user and adds it in address book dict.
    :param address_book: The dictionary with name as key and the email as value.
    :param file_name: The name of the file.
    :return: None
    '''
    # take name and email as input from user
    name = input("Enter name: ")
    email = input("Enter email: ")
    # add name and email in dict
    address_book[name] = email
    with open(file_name, 'w') as f:
        for name,email in address_book.items():
            # add name and email in file
            f.write(f"{name},{email}\n")
    print("Contact added successfully")

def search_contact(address_book):
    '''
    This function displays email by searching with name in the address  dict.

    :param address_book:The dictionary with name as key and the email as value.
    :return: None
    '''
    # take name as input from user
    name = input("Enter name to search: ")
    # print email associated with the name if found
    if name in address_book:
        print(f"Email for {name} is {address_book[name]}.")
    else:
        print(f"Contact not found.")

def list_all_contacts(address_book):
    '''
    This function displays name - email of all contacts in the address book dict.

    :param address_book: The dictionary with name as key and the email as value.
    :return: None
    '''
    # if dict is empty the print no contact else print all the name and email in the dict
    if len(address_book) == 0:
        print("\nNo Contacts")
    else:
        print("\nAll Contacts")
        for name,email in address_book.items():
            print(f"{name} - {email}")

def load_address_book(file_name):
    '''
    This function reads from file and loads name and email in the address book dictionary.
    :param file_name: The name of the file.
    :return: The dictionary loaded with name and email from file.
    '''
    address_book = {}
    try:
        #open file in read mode and print all line from file
        with open(file_name, 'r') as f:
            for line in f:
                #get name and email seperated by , from each line
                name, email = line.strip().split(',')
                # add name and email in dict
                address_book[name] = email
    except FileNotFoundError:
        with open(file_name, 'w') as f:
            pass
    return address_book

def main():
    '''
    This function gives a menu to the user and calls the appropriate functions based on the user's choice.
    '''
    file_name = "address_book.txt"
    address_book = load_address_book(file_name)
    #infinitw loop to give menu to user
    while True:
        print("\nAddress Book Program")
        print("1. Add a new contact")
        print("2. Search for a contact")
        print("3. List all contacts")
        print("4. Quit")
        #take input from user
        user_input = int(input("Enter your choice: "))
        #calls appropriate function based on user's input
        if user_input == 1:
            add_contact(address_book, file_name)
        elif user_input == 2:
            search_contact(address_book)
        elif user_input == 3:
            list_all_contacts(address_book)
        elif user_input == 4:
            print("Thank you!")
            print("Exiting.")
            #exits the loop
            break
        else:
            print("Invalid input.")


if __name__ == "__main__":
    main()