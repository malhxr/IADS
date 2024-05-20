def add_contact(address_book, file_name):
    '''
    This function takes name and email from user and adds it in address book dict.
    :param address_book: The list of dictionaries with name as key and the email as value.
    :param file_name: The name of the file.
    :return: None
    '''
    # take name and email as input from user and remove leading and trailing space
    name = input("Enter name: ").strip()
    email = input("Enter email: ").strip()
    # Check if contact (name and email both) already exist first
    # Name check is case insensitive and email is already in lowercase
    if any(contact['name'].lower() == name.lower() and contact['email'] == email.lower() for contact in address_book):
        print(f"\nContact {name} with email {email} already exists.")
    else:
        #if contact deos not exist the add it in dict and append in list
        address_book.append({'name':name,'email':email.lower()})
        with open(file_name, 'w') as f:
            for contact in address_book:
                f.write(f"{contact['name']},{contact['email']}\n") # write name and email from each dict in addres_book list in file
        print("\nContact added successfully")

def search_contact(address_book):
    '''
    This function displays email by searching with name in the address  dict.

    :param address_book:The list of dictionaries with name as key and the email as value.
    :return: None
    '''
    # if dict is empty then print no contact
    if len(address_book) == 0:
        print("\nNo contacts.\n")
    else:
        #take name of contact to search from user
        name = input("Enter name to search: ")
        count = 0
        #check each element(dict) in list
        for contact in address_book:
            # if name is found in address book then print it with its email
            # searching is by default case insensitive
            if name.lower() == contact['name'].lower():
                count += 1
                print(f"\nEmail for {contact['name']} is {contact['email']}.")
        if count == 0:
            #if no such name is fount then print not found
            print(f"\nContact not found.")

def list_all_contacts(address_book):
    '''
    This function displays name - email of all contacts in the address book dict.

    :param address_book: The list of dictionaries with name as key and the email as value.
    :return: None
    '''
    # if dict is empty the print no contact else print all the name and email in the dict
    if len(address_book) == 0:
        print("\nNo Contacts")
    else:
        print("\nAll Contacts")
        #traverse through list and prints all dict with name and email in it
        for contact in address_book:
            print(f"{contact['name']} - {contact['email']}")

def load_address_book(file_name):
    '''
    This function reads from file and loads name and email in the address book dictionary.
    :param file_name: The name of the file.
    :return: The list of dictionaries loaded with name and email from file.
    '''
    address_book = []
    try:
        #open file in read mode and print all line from file
        with open(file_name, 'r') as f:
            for line in f:
                #get name and email seperated by , from each line of file
                name, email = line.strip().split(',')
                #make a dict of name and email and add it in address book list
                address_book.append({'name':name,'email':email})
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
    #infinite loop to give menu to user and calls function according to their choice
    while True:
        print("\nAddress Book Program")
        print("1. Add a new contact")
        print("2. Search for a contact")
        print("3. List all contacts")
        print("4. Quit")

        #try handles case when user enters non interger value as input
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
