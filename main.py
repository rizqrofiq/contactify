import pyfiglet


def main():
    print(pyfiglet.figlet_format("Contactify"))
    print("Welcome to Contactify: Your personal address book, perfected.")

    print("\nHere are the menu you can choose: ")
    print("1. Show contacts list")
    print("2. Show favorite contacts list")
    print("3. Add contact")
    print("4. Add contact to favorite list")
    print("5. Update contact")
    print("6. Delete contact")


if __name__ == "__main__":
    main()
