import pyfiglet
import inquirer
import os

from contact import Contact
from prettytable import PrettyTable


def main():
    contacts = Contact()
    favorite_contacts = Contact()

    while True:
        os.system("clear")  # Use os.system on Windows

        print(pyfiglet.figlet_format("Contactify"))
        print("Welcome to Contactify: Your personal address book, perfected.")

        print("\nHere are the menu you can choose: ")
        print("1. Show contacts list")
        print("2. Show favorite contacts list")
        print("3. Add contact")
        print("4. Add contact to favorite list")
        print("5. Update contact")
        print("6. Delete contact\n")

        options = inquirer.prompt([
            inquirer.Text(
                "option",
                message="Choose one of the above menu [1/2..]",
                choices=[1, 2, 3, 4, 5, 6],
                validate=lambda _, o: 0 < int(o) <= 6
            )
        ])

        options = int(options["option"])

        if options == 1:
            os.system("clear")
            allContacts = contacts.getAll()

            if len(allContacts) == 0:
                print("\nThere is no contacts available\n")
            else:
                table = PrettyTable()
                table.field_names = [
                    "No", "Name", "Contact Number", "Category"
                ]

                table.add_rows(allContacts)
                print(table)

        elif options == 3:
            os.system("clear")

            print("\nAdd new contact: ")
            contact = inquirer.prompt([
                inquirer.Text("name", message="Name"),
                inquirer.Text("number", message="Number"),
                inquirer.List(
                    "category",
                    message="Type",
                    choices=[
                        ("Landline (Telp. Rumah)", "landline"),
                        ("Mobile Phone", "phone")
                    ],
                ),
            ])

            contacts.append({
                "name": contact["name"],
                "number": contact["number"],
                "category": contact["category"]
            })

            print("Contact address was successfully created")

        input("Press any key to continue...")


if __name__ == "__main__":
    main()
