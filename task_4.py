from collections.abc import Iterator


def parse_input(user_input: str):
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, *args


def add_contact(args: list, contacts: dict) -> str:
    username, phone = args
    if username not in contacts:
        contacts[username] = phone
        return "Contact added."
    return "Contact already exists"


def change_contact(args: list, contacts: dict) -> str:
    username, phone = args
    if username in contacts:
        contacts[username] = phone
        return "Contact updated."
    return "Name is not in contacts. Add new contact"


def show_phone(args: str, contacts: dict) -> str:
    username = args[0]
    if username in contacts:
        return contacts[username]
    return "Name is not in contacts. Add new contact"


def show_all(contacts: dict) -> Iterator:
    return (f"{key} {value}" for key, value in contacts.items())


def main() -> None:
    contacts = {}
    print("Welcome to the assistant bot!")

    while True:
        user_input = input("Enter a command: ")
        command, *args = parse_input(user_input)

        if command in ["close", "exit"]:
            print("Good bye!")
            break

        elif command == "hello":
            print("How can I help you?")
        elif command == "add":
            print(add_contact(args, contacts))
        elif command == "change":
            print(change_contact(args, contacts))
        elif command == "show":
            print(show_phone(args, contacts))
        elif command == "all":
            for contact in show_all(contacts):
                print(contact)
        else:
            print("Invalid command.")


if __name__ == "__main__":
    main()
