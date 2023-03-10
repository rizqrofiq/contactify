import pyfiglet
import inquirer
import os

from contact import Contact
from prettytable import PrettyTable


def main():
    contacts = Contact()
    favorite_contacts = Contact()

    while True:
        os.system("clear")  # Use os.system("cls") on Windows
        print(pyfiglet.figlet_format("Contactify"))
        print("Welcome to Contactify: Your personal address book, perfected.")

        print("\nHere's the menu you can choose: ")
        print("1. Show contacts list")
        print("2. Search Contact")
        print("3. Show favorite contacts list")
        print("4. Add contact")
        print("5. Add contact to favorite list")
        print("6. Update contact")
        print("7. Delete contact")
        print("8. Run Seeder")
        print("9. Exit\n")

        options = inquirer.prompt([
            inquirer.Text(
                "option",
                message="Choose one of the above menu [1/2..]",
                validate=lambda _, o: 0 < int(o) <= 9
            )
        ])

        options = int(options["option"])

        if options == 1:
            os.system("clear")  # Use os.system("cls") on Windows
            allContacts = contacts.getAll()

            if len(allContacts) == 0:
                print("\nThere is no contacts available\n")
            else:
                print("\nHere's all the available contacts: \n")

                table = PrettyTable()
                table.align = "l"
                table.field_names = [
                    "No", "Name", "Contact Number", "Category"
                ]

                table.add_rows(allContacts)
                print(table)

        elif options == 2:
            os.system("clear")  # Use os.system("cls") on Windows

            params = inquirer.prompt([
                inquirer.Text("name", message="Type the name")
            ])

            c = contacts.getByName(params["name"])

            if c is None:
                print(
                    "The contact you've search is not available! Make sure you input the correct name.")
                input("Press any key to continue...")
                continue

            print("\nResult: \n")
            table = PrettyTable()
            table.field_names = ["Name", "Contact Number", "Category"]
            table.align = "l"

            table.add_row([
                c.data["name"],
                c.data["number"],
                c.data["category"]
            ])

            print(table)

        elif options == 3:
            os.system("clear")  # Use os.system("cls") on Windows
            allFavoriteContacts = favorite_contacts.getAll()

            if len(allFavoriteContacts) == 0:
                print("\nThere is no favorite contacts\n")
            else:
                print("\nHere's all the available favorite contacts: \n")

                table = PrettyTable()
                table.align = "l"
                table.field_names = [
                    "No", "Name", "Contact Number", "Category"
                ]

                table.add_rows(allFavoriteContacts)
                print(table)

        elif options == 4:
            os.system("clear")  # Use os.system("cls") on Windows

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

        elif options == 5:
            os.system("clear")  # Use os.system("cls") on Windows

            params = inquirer.prompt([
                inquirer.Text("name", message="Type the name")
            ])

            c = contacts.getByName(params["name"])

            if c is None:
                print(
                    "The contact you've selected is not available! Make sure you input the correct name.")
                input("Press any key to continue...")
                continue

            print("\nThis is the contact you've selected: \n")
            table = PrettyTable()
            table.field_names = ["Name", "Contact Number", "Category"]
            table.align = "l"

            table.add_row([
                c.data["name"],
                c.data["number"],
                c.data["category"]
            ])

            print(table)

            add = inquirer.confirm(
                f"Are you sure want to add {c.data['name']}'s contact to favorites?",
                default=False
            )

            if add:
                favorite_contacts.append({
                    "name": c.data["name"],
                    "number": c.data["number"],
                    "category": c.data["category"]
                })

                print("Contact has been succesfully added to favorite")
            else:
                print("Cancelled")

        elif options == 6:
            os.system("clear")  # Use os.system("cls") on Windows

            params = inquirer.prompt([
                inquirer.Text("name", message="Type the name")
            ])

            (index, c) = contacts.getIndexByName(params["name"])

            if c is None:
                print(
                    "The contact you've selected is not available! Make sure you input the correct name.")
                input("Press any key to continue...")
                continue

            print("\nThis is the contact you've selected: \n")
            table = PrettyTable()
            table.field_names = ["Name", "Contact Number", "Category"]
            table.align = "l"

            table.add_row([
                c.data["name"],
                c.data["number"],
                c.data["category"]
            ])

            print(table)

            newData = inquirer.prompt([
                inquirer.Text("name", message="New name"),
                inquirer.Text("number", message="New Number"),
                inquirer.List(
                    "category",
                    message="New category",
                    choices=[
                        ("Landline (Telp. Rumah)", "landline"),
                        ("Mobile Phone", "phone")
                    ],
                )
            ])

            add = inquirer.confirm(
                f"Are you sure want to update this contact?",
                default=False
            )

            if add:
                update = contacts.update(index, {
                    "name": newData["name"],
                    "number": newData["number"],
                    "category": newData["category"]
                })

                if update:
                    print("Contact has been successfully updated")
                else:
                    print("An error has occured")
            else:
                print("Cancelled")

        elif options == 7:
            os.system("clear")  # Use os.system("cls") on Windows

            params = inquirer.prompt([
                inquirer.Text("name", message="Type the name")
            ])

            (index, c) = contacts.getIndexByName(params["name"])

            if c is None:
                print(
                    "The contact you've selected is not available! Make sure you input the correct name.")
                input("Press any key to continue...")
                continue

            print("\nThis is the contact you've selected: \n")
            table = PrettyTable()
            table.field_names = ["Name", "Contact Number", "Category"]
            table.align = "l"

            table.add_row([
                c.data["name"],
                c.data["number"],
                c.data["category"]
            ])

            print(table)

            confirm = inquirer.confirm(
                f"Are you sure want to delete this contact?",
                default=False
            )

            if confirm:
                delete = contacts.remove_at_index(index)

                if delete:
                    print("Contact has been successfully deleted")
                else:
                    print("An error has occured")
            else:
                print("Cancelled")

        elif options == 8:
            contacts.seed()
            contacts.print_list()

        elif options == 9:
            print("Thank you for using this program. Bye!")
            break

        input("Press any key to continue...")


if __name__ == "__main__":
    main()
