print("...SIMPLE CONTACT SAVER...")

while True:
    contact_option = input("Select:\n 1. Add new Contact \n 2. View all Contact \n 3. Exit \n")
    if contact_option == "1":
        name = input("Text in Name: ")
        number = input("Enter in Number: ")
        with open("contact.txt, a") as sfile:
            sfile.write(f"{name} - {number}")
            sfile.close()
            print("Contact Saved!")
    elif contact_option == "2":
        try:
            with open("contact.txt, r") as sfile:
                contacts = file.read()
                if contacts:
                    print("All Contacts.")
                    print(contacts)
                else:
                    print("No Contact Saved!!")
        except:
            print("No Saved Contact, try saving.")
        finally:
            file.close()
    elif contact_option == "3":
        print("Exiting....")
        break
    else:
        print("Invalid!!, Try again.")

